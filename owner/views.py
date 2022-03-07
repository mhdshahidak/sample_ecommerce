from django.shortcuts import render

from seller import views

# Create your views here.
def owner_home(request):
    return render(request,'owner_home.html')

def new_seller(request):
    return render(request,'new_seller.html')

def customer(request):
    return render(request,'customer.html')

def sellers(request):
    return render(request,'sellers.html')