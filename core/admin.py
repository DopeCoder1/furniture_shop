from django.contrib import admin
from .models import *
# Register your models here.

class FurnitureAdmin(admin.ModelAdmin):
    search_fields = ("name","category")
    list_display = ("name","category","price","created_at")
    list_filter = ("name","category","price")

class OrderAdmin(admin.ModelAdmin):
    search_fields = ("name","customer")
    list_display = ("id","name","customer","email")
    list_filter = ("name","customer","email")



admin.site.register(Profile)
admin.site.register(Furniture,FurnitureAdmin)
admin.site.register(Category)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)