import email
from webbrowser import get
from django.shortcuts import redirect, render
from . models import *

# Create your views here.

# home


def home(request):
    return render(request, 'home.html')

# seller registration


def seller_reg(request):
    msg = ""

    if request.method == 'POST':

        name = request.POST['seller_name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        acc_holder = request.POST['acc_holder']
        acc_no = request.POST['acc_no']
        ifsc = request.POST['ifsc']
        password = request.POST['password']

        # to check whether it is exist or not

        email_exist = Seller.objects.filter(email_id=email).exists()

        if not email_exist:
            new_seller = Seller(seller_name=name, email_id=email, acc_holder=acc_holder,
                                acc_no=acc_no, ifsc=ifsc, phone_no=phone_no, password=password)
            new_seller.save() #insert into table tablename
            msg = "registerd successfully"

        else:
            msg = "email already exist"

    return render(request, 'seller_reg.html', {'msg': msg, })

# for customer registration


def customer_reg(request):
    msg = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone']
        password = request.POST['password']
        email_exist = Customer.objects.filter(email_id=email).exists()

        if not email_exist:
            new_customer = Customer(
                cust_name=name, email_id=email, phone_no=phone_no, password=password)
            new_customer.save()
            msg = 'Registered succesfully'

        else:
            msg = "email already exist"

    return render(request, 'customer_reg.html', {'msg': msg, })

# customer resitration


def customer_login(request):
    msg = ""

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        customer_exist = Customer.objects.filter(
            email_id=email, password=password).exists()
        if customer_exist:
            customer_data = Customer.objects.get(
                email_id=email, password=password)
            request.session['customer'] = customer_data.cust_id
            return redirect('customer:customerhome')

        else:
            msg = "user name or password incorrect"
            return render(request, 'customer_login.html')

    return render(request, 'customer_login.html', {'msg': msg, })


def seller_login(request):
    msg = ""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        seller_exist = Seller.objects.filter(
            email_id=email, password=password).exists()
        if seller_exist:
            seller_data = Seller.objects.get(email_id=email, password=password)
            request.session['seller'] = seller_data.seller_id
            return redirect('seller:sellerhome')

        else:
            msg = "user name or password incorrect"
            return render(request, 'seller_login.html', {'msg': msg, })

    return render(request, 'seller_login.html')