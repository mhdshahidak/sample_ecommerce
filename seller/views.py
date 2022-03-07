from django.shortcuts import render


# Create your views here.
def seller_login(request):
    return render(request,'login.html')

def seller_home(request):
    return render(request,'seller_home.html')

def add_product(request):
    return render(request,'add_product.html')

def view_product(request):
    return render(request,'view_product.html')

def view_order(request):
    return render(request,'view_order.html')

def change_password(request):
    return render(request,'change_password.html')