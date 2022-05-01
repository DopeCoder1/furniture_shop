from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    photo = models.ImageField(upload_to="user_photos/%Y/%m/%d/", verbose_name="Фото")
    iin = models.CharField(max_length=20,verbose_name="ИИН:")
    bank_iin = models.CharField(max_length=20,verbose_name='Банковский счет')
    def save(self, *args, **kwargs):
        super().save()

class Furniture(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Последний изм.")
    rating = models.IntegerField(default=5,verbose_name="rating")
    published_status = models.IntegerField(default=0, verbose_name="Публиковать?")
    desc = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебели"



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"





class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=150)
    account_no = models.CharField(max_length = 20)
    bank_no = models.CharField(max_length = 20)
    totalfurniture = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField("Статус",default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
