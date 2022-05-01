from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User, Group
from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from core.cart import Cart
from core.forms import ProfileUserForm, ProfielExtrForm, LoginForm, ProfileUpdateForm, ProfileUpdateExtraForm, \
    OrderCreateForm
from core.models import  Profile, OrderItem,Category, Furniture


def is_profile(user):
    return user.groups.filter(name='CLIENT').exists()


def afterlogin_view(request):
    if is_profile(request.user):
        accountapproval=Profile.objects.all().filter(user_id=request.user.id)
        if accountapproval:
            return redirect('account')




def index(request):
    cart = Cart(request)
    books = Furniture.objects.all()
    category = Category.objects.all()
    context = {
        "card":cart,
        "category":category,
        "books":books,
    }
    return render(request, "core/index.html", context)


@user_passes_test(is_profile)
def account(request):
    category = Category.objects.all()
    users = Profile.objects.get(user_id=request.user.id)
    order_item = OrderItem.objects.filter(order__customer_id=request.user.id)
    buy_fur_count = OrderItem.objects.filter(order__customer_id=request.user.id).count()
    context = {
        "category":category,
        "buy_fur_count":buy_fur_count,
        "users":users,
        "order_item":order_item,
    }
    return render(request, 'core/account.html', context)



def details(request,id):
    category = Category.objects.all()
    books = get_object_or_404(Furniture,id=id)
    context={
        "category":category,
        "books":books
    }
    return render(request, "core/detail.html", context)


def categoryies(request,id):
    category = Category.objects.all()
    books = Furniture.objects.filter(category_id=id)
    context = {
        "category":category,
        "books":books,
    }
    return render(request, "core/index.html", context)


def cart_details(request):
    category = Category.objects.all()
    cart = Cart(request)
    context = {
        "category":category,
        "cart": cart,
    }
    return render(request, 'core/cart.html', context)

def cart_remove(request, bookid):
    cart = Cart(request)
    book = get_object_or_404(Furniture, id=bookid)
    cart.remove(book)
    return redirect('card_details')

def cart_add(request, bookid):
    cart = Cart(request)
    book = get_object_or_404(Furniture, id=bookid)
    cart.add(book=book)

    return redirect('card_details')


def cart_update(request, bookid, quantity):
    cart = Cart(request)
    book = get_object_or_404(Furniture, id=bookid)
    cart.update(book=book, quantity=quantity)
    price = (book.price * quantity)

    return render(request, 'core/cart.html', {"price": price})


def order_create(request):
	cart = Cart(request)
	if request.user.is_authenticated:
		customer = get_object_or_404(User, id=request.user.id)
		form = OrderCreateForm(request.POST or None, initial={"name": customer.first_name, "email": customer.email})
		if request.method == 'POST':
			if form.is_valid():
				order = form.save(commit=False)
				order.customer = User.objects.get(id=request.user.id)
				order.payable = cart.get_total_price()
				order.totalfurniture = len(cart) # len(cart.cart) // number of individual book
				order.save()

				for item in cart:
					OrderItem.objects.create(
						order=order,
					    furniture=item['book'],
						price=item['price'],
						quantity=item['quantity']
						)
				cart.clear()
				return render(request, 'core/scc.html', {'order': order})

			else:
				messages.error(request, "Fill out your information correctly.")

		if len(cart) > 0:
			return render(request, 'core/chec.html', {"form": form})
		else:
			return redirect('home')
	else:
		return redirect('login')


def registration(request):
    form = ProfileUserForm()
    form2 = ProfielExtrForm()
    category = Category.objects.all()
    if request.method == "POST":
        form = ProfileUserForm(request.POST)
        form2 = ProfielExtrForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            user2 = form2.save(commit=False)
            user2.user = user
            user2.save()
            my_profile_group = Group.objects.get_or_create(name="CLIENT")
            my_profile_group[0].user_set.add(user)
            return redirect("home")

    context = {
        "form":form,
        "form2":form2,
    }
    return render(request, "core/register.html", context)

def logins(request):
    form3 = LoginForm()
    if request.method == "POST":
        form3 = LoginForm(request.POST)
        if form3.is_valid():
            user3 = authenticate(username=form3.cleaned_data['username'], password=form3.cleaned_data['password'])
            if user3 is not None:
                login(request, user3)
                return redirect("afterlogin")

    context = {
        "form3":form3
    }
    return render(request, 'core/login.html', context)