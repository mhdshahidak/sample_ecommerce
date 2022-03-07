from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customer_home.html')

def view_cart(request):
    return render(request,'view_cart.html')

def profile(request):
    return render(request,'profile.html')

def my_order(request):
    return render(request,'my_order.html')

# def logout(request):
#     return render(request,'logut.html')