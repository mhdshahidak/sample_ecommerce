from django.shortcuts import redirect
from email import message
from django.shortcuts import render
from common.models import Seller
from customer.models import Order, Cart
from ecom.decorators import auth_seller

from seller.models import Products


# Create your views here
# def seller_login(request):
#     return render(request, 'login.html')

@auth_seller
def seller_home(request):
    seller = Seller.objects.get(seller_id=request.session['seller'])
    products = Products.objects.filter(seller_id=request.session['seller'])
    return render(request, 'seller_home.html', {'seller': seller, 'product': products})


@auth_seller
def add_product(request):
    msg = ""
    if request.method == 'POST':
        product_name = request.POST['pname']
        price = request.POST['pprice']
        description = request.POST['pdescription']
        qty = request.POST['pquantity']
        image = request.FILES['pimg']
        # taking row(object) from table
        seller = Seller.objects.get(seller_id=request.session['seller'])

        new_product = Products(product_name=product_name, price=price,
                               description=description, stock=qty, product_image=image, seller_id=seller)
        new_product.save()
        msg = "product addedd succusfully"
    return render(request, 'add_product.html', {'msg': msg})


@auth_seller
def view_product(request):

    seller_product = Products.objects.filter(
        seller_id=request.session['seller'])
    seller = Seller.objects.get(seller_id=request.session['seller'])  # ///
    return render(request, 'view_products.html', {'products': seller_product, 'seller': seller})


@auth_seller
def view_order(request):

    orders = Order.objects.filter(
        seller_id=request.session['seller'], status="ordered")

    return render(request, 'view_order.html', {'orders': orders, })


@auth_seller
def change_password(request):
    msg = ""
    if request.method == 'POST':
        password = request.POST['password']
        newpassword = request.POST['newpassword']
        cpassword = request.POST['cpassword']

        seller_data = Seller.objects.get(seller_id=request.session['seller'])
        # first 'password': variable that gets old password & second password is model proparty
        if password == seller_data.password:

            if newpassword == cpassword:
                seller_data.password = newpassword  # updation
                seller_data.save()
                msg = "successfully updated"
            else:
                msg = "password mismatch"
        else:
            msg = "password incorrect"

    return render(request, 'change_password.html', {'msg': msg, })


@auth_seller
def logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('common:sellerlogin')
