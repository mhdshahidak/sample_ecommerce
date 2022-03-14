# from django.http import HttpResponse
from django.shortcuts import render, redirect
from common.models import Customer, Seller
from customer.models import Order
from customer.models import Cart
from ecom.decorators import auth_customer

from seller.models import Products

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

@auth_customer
def customer_home(request):

    
    customer = Customer.objects.get(cust_id=request.session['customer'])
        
    return redirect('common:customerlogin')

@auth_customer
def view_cart(request):

    cart_products = Cart.objects.filter(
        customer_id=request.session['customer'])
    return render(request, 'view_cart.html', {'cartproduct': cart_products})


def order(request, pid):
    msg = ""
    product = Products.objects.get(id=pid)
    if request.method == 'POST':

        customer_id = Customer.objects.get(cust_id=request.session['customer'])  #session
        seller_id = Seller.objects.get(seller_id=product.seller_id.seller_id)
        quantity = request.POST['quantity']
        ship_address = request.POST['address']
        total = int(quantity)*product.price

        orders = Order(product_id=product, customer_id=customer_id, seller_id=seller_id,
                       quantity=quantity, shipping_address=ship_address, total_amount=total)
        orders.save()
        msg = "ordered"

        product.stock = product.stock-int(quantity)
        product.save()

        send_mail("oreder details", " your order placed successfully",
                  settings.EMAIL_HOST_USER, [str(customer_id.email_id)])

        return redirect('customer:customerhome')

    return render(request, 'order.html', {'msg': msg, 'product': product})


def my_order(request):

    orders = Order.objects.filter(customer_id=request.session['customer'])
    return render(request, 'my_order.html',{'orders':orders,})


def change_password(request):
    msg = ""
    if request.method == 'POST':
        oldpassword = request.POST['password']
        newpassword = request.POST['newpassword']
        cpassword = request.POST['cpassword']

        customer_data = Customer.objects.get(
            cust_id=request.session['customer'])

        if customer_data.password == oldpassword:
            if newpassword == cpassword:
                Customer.objects.filter(cust_id=request.session['customer']).update(
                    password=newpassword)  # direct updation
                msg = "updated successfully"
            else:
                msg = "missmatch"
        else:
            msg = "incorrect password.."

    return render(request, 'change_password.html', {'msg': msg, })


def add_to_cart(request, id):

    # first id from produst table second from id passing
    product_id = Products.objects.get(id=id)
    customer_id = Customer.objects.get(cust_id=request.session['customer'])

    cart_exist = Cart.objects.filter(
        customer_id=request.session['customer'], product_id=product_id).exists()

    if not cart_exist:
        new_cart = Cart(product_id=product_id, customer_id=customer_id)
        new_cart.save()

    return redirect('customer:customerhome')


def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:customerlogin')
