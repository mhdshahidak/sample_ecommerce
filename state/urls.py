from django.urls import path
from . import views

app_name = 'state'

urlpatterns = [
    path('', views.dropdown, name="dropdown"),
    path('statecheck', views.state_check, name="statecheck"),
    
]