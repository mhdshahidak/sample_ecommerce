from django.shortcuts import render
from common.models import Seller

from seller.models import Products


# Create your views here.
def seller_login(request):
    return render(request, 'login.html')


def seller_home(request):
    return render(request, 'seller_home.html')


def add_product(request):
    msg = ""
    if request.method == 'POST':
        product_name = request.POST['pname']
        price = request.POST['pprice']
        description = request.POST['pdescription']
        qty = request.POST['pquantity']
        image = request.FILES['pimg']
        seller = Seller.objects.get(seller_id=request.session['seller'])

        new_product = Products(product_name=product_name, price=price,
                               description=description, stock=qty, product_image=image, seller_id=seller)
        new_product.save()
        msg = "product addedd succusfully"
    return render(request, 'add_product.html', {'msg': msg})


def view_product(request):

    seller_product = Products.objects.filter(
        seller_id=request.session['seller'])
    seller = Seller.objects.get(seller_id=request.session['seller'])
    return render(request, 'view_products.html', {'products': seller_product, 'seller': seller})


def view_order(request):
    return render(request, 'view_order.html')


def change_password(request):
    return render(request, 'change_password.html')
