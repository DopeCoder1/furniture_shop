from unicodedata import name

from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('account/', account, name = 'account'),
    path('details/<int:id>/', details, name = 'details'),
    path("exit/", LogoutView.as_view(), name="exit"),
    path('afterlogin', afterlogin_view, name='afterlogin'),
    path("categoryies/<int:id>/",categoryies,name="category"),
    path("card_add/<int:bookid>/",cart_add,name="card_add"),
    path("card_details",cart_details,name="card_details"),
    path("card_remove/<int:bookid>/",cart_remove,name="card_remove"),
    path('card_update/<int:bookid>/<int:quantity>/', cart_update, name='cart_update'),
    path('registration/',registration,name="registration"),
    path('login/',logins,name='login'),
    path('order_create/', order_create, name='order_create'),


]
