from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('',views.owner_home,name="ownerhome"),
    path('customer/',views.customer,name="customer"),
    path('newseller/',views.new_seller,name="newseller"),
    path('sellers/',views.sellers,name="sellers"),
]