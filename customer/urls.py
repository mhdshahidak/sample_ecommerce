from unicodedata import name
from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('customerhome', views.customer_home, name="customerhome"),
    path('viewcart', views.view_cart, name="viewcart"),
    path('myorder', views.my_order, name="myorder"),
    path('changepassword', views.change_password, name='changepassword'),
    path('cart/<int:id>',views.add_to_cart,name="addtocart"),
    path('logout',views.logout, name="logout"),
    path('order/<int:pid>',views.order, name="order"),

]
