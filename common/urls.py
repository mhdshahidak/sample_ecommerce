from unicodedata import name
from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.home, name='commonhome'),
    path('sellerreg', views.seller_reg, name='sellerreg'),
    path('customerreg', views.customer_reg, name='customerreg'),
    path('sellerlogin', views.seller_login, name='sellerlogin'),
    path('customerlogin', views.customer_login, name='customerlogin'),
    path('checkselleremail', views.check_seller_email, name="checksellermail"),
    path('checkcustomeremail', views.check_customer_email,
         name="checkcustomeremail"),
]
