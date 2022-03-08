from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('customerhome', views.customer_home, name="customerhome"),
    path('viewcart', views.view_cart, name="viewcart"),
    path('profile', views.profile, name="profile"),
    path('myorder', views.my_order, name="myorder"),
]
