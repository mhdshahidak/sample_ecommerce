from email import message
from email.policy import EmailPolicy
from webbrowser import get
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view  # for api connection
from rest_framework.response import Response    # for api response

from common.forms import CustomerRegForm
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

        # filter() multiple data according to the where condition select * from table where pricxe =5000
        email_exist = Seller.objects.filter(email_id=email).exists()

        if not email_exist:
            new_seller = Seller(seller_name=name, email_id=email, acc_holder=acc_holder,
                                acc_no=acc_no, ifsc=ifsc, phone_no=phone_no, password=password)
            new_seller.save()  # insert into table tablename
            msg = "registerd successfully"

        else:
            msg = "email already exist"

    return render(request, 'seller_reg.html', {'msg': msg, })

# for customer registration


def customer_reg(request):
    msg = ""
    form = CustomerRegForm()
    if request.method == 'POST':
        # ,request.files  if files need to upload
        form = CustomerRegForm(request.POST)
        if form.is_valid():
            name = request.POST['cust_name']
            email = request.POST['email_id']
            phone_no = request.POST['phone_no']
            password = request.POST['password']
            email_exist = Customer.objects.filter(email_id=email).exists()

            if not email_exist:
                new_customer = Customer(
                    cust_name=name, email_id=email, phone_no=phone_no, password=password)
                new_customer.save()
                form = CustomerRegForm()
                msg = 'Registered succesfully'

            else:
                msg = "email already exist"

        else:
            print(form.errors)

    # {'msg': msg, } for massage passing
    return render(request, 'customer_reg.html', {'msg': msg, 'form': form})

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
            # passing customer id as session value
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
            # redirecting to seller home page  # app name : url name
            return redirect('seller:sellerhome')

        else:
            msg = "user name or password incorrect"
            return render(request, 'seller_login.html', {'msg': msg, })

    return render(request, 'seller_login.html')


def check_seller_email(request):
    email = request.GET['email']  # get method
    seller_exist = Seller.objects.filter(
        email_id=email).exists()
    if seller_exist:
        status = True
    else:
        status = False
    return JsonResponse({'status': status, 'email': email})


def check_customer_email(request):
    email = request.POST['email']  # post method
    customer_exists = Customer.objects.filter(email_id=email).exists()
    if customer_exists:
        status = True
    else:
        status = False
    return JsonResponse({'status': status, 'email': email})

#api connectio

@api_view(['GET', 'POST'])
def apifn(request):
    if request.method == 'POST':


        # data = request.data
        # print(data['username'])
        # username = data['username']
        # password = data['password']

        # app = Apiusers(user_name=username,password=password) inserting data into database
        # app.save()

        # serial

        return Response({'status':'data entered successfully',})
    else:
        return Response({'name':'shd', 'username':'shd@gmail.com'})