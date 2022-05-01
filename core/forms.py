from django import forms
from django.contrib.auth.models import User

from core.models import Profile
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'account_no','bank_no']


class ProfileUserForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={"class":"input100","placeholder": "Имя","required class":"registration_inputs"}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={"class":"input100","placeholder": "Фамилия","required class":"registration_inputs"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class":"input100","placeholder": "Почта","required class":"registration_inputs"}))
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class":"input100","placeholder": "Логин","required class":"registration_inputs"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class":"input100","placeholder": "Пароль","required class":"registration_inputs"}))

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]

class ProfielExtrForm(forms.ModelForm):
    address = forms.CharField(label="Адрес",widget=forms.TextInput(attrs={"class":"input100","placeholder":"Адрес","required class":"registration_inputs"}))
    photo = forms.ImageField(label="Фото",widget=forms.FileInput(attrs={"class":"input100","placeholder":"Фото","required class":"registration_inputs"}))
    iin = forms.CharField(label="ИИН",widget=forms.TextInput(attrs={"class":"input100","placeholder":"Иин","required class":"registration_inputs"}))
    bank_iin = forms.CharField(label="Банковский счет",widget=forms.TextInput(attrs={"class":"input100","placeholder":"Банковский счёт","required class":"registration_inputs"}))

    class Meta:
        model = Profile
        fields = ["address","photo","iin","bank_iin"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"input100","placeholder":"Логин","required class":"registration_inputs"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class":"input100","placeholder":"Пароль","required class":"registration_inputs"}))


class ProfileUpdateForm(forms.Form):
    username = forms.CharField(label="Логин",required=True, widget=forms.TextInput(
        attrs={"placeholder": "Логин", "required class": "registration_inputs"}))
    email = forms.EmailField(label="Email",required=True, widget=forms.EmailInput(
        attrs={"placeholder": "Почта", "required class": "registration_inputs"}))

    class Meta:
        model = User
        fields = ["username","email"]


class ProfileUpdateExtraForm(forms.ModelForm):
    address = forms.CharField(label="Адрес", widget=forms.TextInput(
        attrs={"placeholder": "Адрес", "required class": "registration_inputs"}))
    photo = forms.ImageField(label="Фото", widget=forms.FileInput(
        attrs={"placeholder": "Фото", "required class": "registration_inputs"}))
    iin = forms.CharField(label="ИИН",
                          widget=forms.TextInput(attrs={"placeholder": "Иин", "required class": "registration_inputs"}))
    bank_iin = forms.CharField(label="Банковский счет", widget=forms.TextInput(
        attrs={"placeholder": "Банковский счёт", "required class": "registration_inputs"}))

    class Meta:
        model = Profile
        fields = ["address", "photo", "iin", "bank_iin"]

