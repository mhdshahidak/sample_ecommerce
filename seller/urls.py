from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('', views.seller_login, name='login'),
    path('sellerhome', views.seller_home, name='sellerhome'),
    path('addproduct', views.add_product, name='addproduct'),
    path('viewproduct', views.view_product, name='viewproduct'),
    path('vieworder', views.view_order, name='vieworder'),
    path('changepassword', views.change_password, name='changepassword'),
    path('logout',views.logout, name="logout"),
]
