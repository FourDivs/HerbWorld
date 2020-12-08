from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer, Manager, Order, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'herbworldapp/home.html')


def contactUs(request):
    return render(request, 'herbworldapp/contact.html')


def about(request):
    return render(request, 'herbworldapp/about.html')


def loginHome(request):
    return render(request, 'herbworldapp/loginhome.html')


def logoutHome(request):

    logout(request)

    return redirect('/')


def managerLogin(request):
    if request.method == 'POST':
        username = request.POST['managerloginusername']
        password = request.POST['managerloginpassword']
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/')


def managerSignup(request):
    if request.method == 'POST':
        username = request.POST['managersignupusername']
        nursery_name = request.POST['managernurseryname']
        first_name = request.POST['managersignupfirstname']
        last_name = request.POST['managersignuplastname']
        email = request.POST['managersignupemail']
        phone = request.POST['managersignupphone']
        password = request.POST['managersignuppassword']
        # profile_image = request.FILES['doctor_image']

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        userdata = Manager(phone=phone, user=user, nursery_name=nursery_name)
        userdata.save()

        return redirect('/')


def customerLogin(request):
    if request.method == 'POST':
        username = request.POST['customerloginusername']
        password = request.POST['customerloginpassword']
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/')


def customerSignup(request):
    if request.method == 'POST':
        username = request.POST['customersignupusername']
        first_name = request.POST['customersignupfirstname']
        last_name = request.POST['customersignuplastname']
        email = request.POST['customersignupemail']
        phone = request.POST['customersignupphone']
        password = request.POST['customersignuppassword']
        # profile_image = request.FILES['doctor_image']

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        userdata = Customer(phone=phone, user=user)
        userdata.save()

        return redirect('/')


def manageProducts(request):
    props = Product.objects.filter(
        nursery_id=request.user.username)
    return render(request, 'herbworldapp/manageproducts.html', {'props': props})


def addProduct(request):
    if request.method == 'POST':
        name = request.POST['productname']
        price = request.POST['productprice']
        quantity = request.POST['productquantity']
        product_id = request.POST['productid']
        description = request.POST['productdescription']
        nursery_id = request.user.username

        productdata = Product(name=name, price=price, quantity=quantity,
                              product_id=product_id, description=description, nursery_id=nursery_id)
        productdata.save()
        return redirect('/manageproducts')


def nurseryList(request):
    props = Manager.objects.all()
    return render(request, 'herbworldapp/nurserylist.html', {'props': props})


def showNurseryProducts(request, username):
    props = Product.objects.filter(nursery_id=username)
    return render(request, 'herbworldapp/productlist.html', {'props': props})

def delProduct(request):
    if request.method == 'POST':
        del_prodID = request.POST['productid']
        #del_prodID = int(del_prodID)
        delete_prod = Product.objects.get(product_id = del_prodID)
        delete_prod.delete()
        props = Product.objects.filter(nursery_id=request.user.username)
        return redirect('/manageproducts')

def createOrder(request):
    if request.method == 'POST':
        order_id = len(Order.objects.all()) + 1
        product_id = request.POST['productid']
        nursery_id = request.POST['nurseryid']
        customer_id = request.user.username
        email = request.POST['customeremail']
        phone = request.POST['customerphone']
        quantity = int(request.POST['productquantity'])
        price = request.POST['productprice']
        address = request.POST['customeraddress']
        
        order_total = int(price)*int(quantity)

        orderdata = Order(order_id=order_id, product_id=product_id, nursery_id=nursery_id,
                          customer_id=customer_id, email=email, phone=phone, quantity=quantity, order_total=order_total, address=address)
        orderdata.save()
        return redirect('/')

def updateProduct(request):
    if request.method == 'POST':
        product_id = request.POST['productid']
        product_name = request.POST['productname']
        quantity = int(request.POST['productquantity'])
        price = request.POST['productprice']
        desc = request.POST['productdescription']

        Product.objects.filter(product_id=product_id).update(name=product_name, price=price, quantity=quantity,
                               description=desc)
        
        return redirect('/manageproducts')


def myOrders(request):
    props = Order.objects.filter(customer_id=request.user.username)
    return render(request, 'herbworldapp/orderlist.html', {'props': props})

def cancelOrder(request):
    if request.method == 'POST':
        cancel_orderID = request.POST['orderid']
        cancel_orderID = int(cancel_orderID)
        cancel_order = Order.objects.get(order_id = cancel_orderID)
        cancel_order.delete()
        props = Order.objects.filter(customer_id=request.user.username)
        return redirect('/')

def manageOrders(request):
    props = Order.objects.filter(nursery_id=request.user.username)
    return render(request, 'herbworldapp/orderlist.html', {'props': props})
