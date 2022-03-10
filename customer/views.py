from django.http import HttpResponse
from django.shortcuts import render,redirect
from common.models import Customer
from customer.models import Cart

from owner.views import customer
from seller.models import Products
# Create your views here.


def customer_home(request):
    customer = Customer.objects.get(cust_id =request.session['customer'])
    products = Products.objects.all()
    return render(request, 'customer_home.html', {'customer': customer,'product':products})


def view_cart(request):

    cart_products = Cart.objects.filter(customer_id=request.session['customer'])
    return render(request, 'view_cart.html',{'cartproduct':cart_products})


def profile(request):
    return render(request, 'profile.html')


def my_order(request):
    return render(request, 'my_order.html')

# def logout(request):
#     return render(request,'logut.html')

def change_password(request):
    msg = ""
    if request.method=='POST':
        oldpassword = request.POST['password']
        newpassword = request.POST['newpassword']
        cpassword = request.POST['cpassword']

        customer_data = Customer.objects.get(cust_id=request.session['customer'])

        if customer_data.password==oldpassword:
            if newpassword==cpassword:
                Customer.objects.filter(cust_id=request.session['customer']).update(password=newpassword) #direct updation
                msg="updated successfully"
            else:
                msg="missmatch"
        else:
            msg="incorrect password.."


        

    

    return render(request, 'change_password.html',{'msg':msg,})

def add_to_cart(request,id):

    product_id = Products.objects.get(id=id)      #first id from produst table second from id passing
    customer_id = Customer.objects.get(cust_id=request.session['customer'])

    cart_exist=Cart.objects.filter(customer_id=request.session['customer'],product_id=product_id).exists()

    if not cart_exist:
        new_cart = Cart(product_id=product_id,customer_id=customer_id)
        new_cart.save()

    
    

    return redirect('customer:customerhome')

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:customerlogin')
    
    
