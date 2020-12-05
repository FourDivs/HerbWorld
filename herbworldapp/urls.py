from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [

    # HOME PAGE URLS
    path('', views.home, name="home"),
    path("about/", views.about, name="AboutUs"),
    path("contactus/", views.contactUs, name="contactUs"),
    path("login/", views.loginHome, name="loginHome"),
    path("login/managerlogin", views.managerLogin, name="managerLogin"),
    path("login/managersignup", views.managerSignup, name="managerSignup"),
    path("login/customerlogin", views.customerLogin, name="customerLogin"),
    path("login/customersignup", views.customerSignup, name="customerSignup"),
    path("logout/", views.logoutHome, name="logout"),



    path("myorders/", views.myOrders, name="myOrders"),
    path("myorders/cancelorder", views.cancelOrder, name="cancelOrder"),
    path("manageorders/", views.manageOrders, name="manageOrders"),



    path("manageproducts/", views.manageProducts, name="manageProducts"),
    path("manageproducts/addproduct", views.addProduct, name="addProduct"),


    path("nurserylist/", views.nurseryList, name="nurseryList"),
    path("nurserylist/order", views.createOrder, name="createOrder"),
    path("nurserylist/<username>", views.showNurseryProducts,
         name="showNurseryProducts")




]
