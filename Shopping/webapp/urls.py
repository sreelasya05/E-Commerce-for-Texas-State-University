"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [


    path('', views.home, name="home"),
    path('adminlogin/', views.adminlogin, name="adminlogin"), 
    path('adminhome/', views.adminhomedef, name="adminhome"),
    path('adminlogout/', views.adminlogoutdef, name="adminlogout"),
    path('ulogin/', views.userlogindef, name="userlogindef"),    
    path('userreg/', views.signupdef, name="signupdef"),    
    path('usignupaction/', views.usignupactiondef, name="usignupactiondef"),
    path('usignupaction2/', views.usignupaction2def, name="usignupaction2"),
    path('userloginaction/', views.userloginactiondef, name="userloginactiondef"),
    path('userhome/', views.userhomedef, name="userhome"),
    path('userlogout/', views.userlogoutdef, name="userlogout"),

    
    path('forget/', views.forget, name="forget"),
    path('forget2/', views.forget2, name="forget2"),
    path('forget3/', views.forget3, name="forget3"),


    path('addcategory/', views.addcategory, name="addcategory"),
    path('addcataction/', views.addcataction, name="addcataction"),
    path('additem/', views.additem, name="additem"),
    path('additemaction/', views.additemaction, name="additemaction"),

    path('uviewproducts/<str:cid>/', views.uviewproducts, name="uviewproducts"),
    path('viewsingle/<str:pid>/', views.viewsingle, name="viewsingle"),
    path('addtocart/', views.addtocart, name="addtocart"),
    path('cartview/', views.cartview, name="cartview"),
    path('cartdelete/<str:op>/', views.cartdelete, name="cartdelete"),
    path('payment/', views.payment, name="payment"),

    path('chatpage/', views.chatpagestart, name="chatpagestart"),
    path('chatload/', views.chatload, name="chatload"),
    path('chataction/', views.chataction, name="chataction"),


    path('viewfeedback/', views.viewfeedback, name="viewfeedback"),
    path('addfeedback/', views.addfeedback, name="addfeedback"),
    path('addrequest/', views.addrequest, name="addrequest"),
    path('viewalerts/', views.viewalerts, name="viewalerts"),
    path('vieworders/', views.vieworders, name="vieworders"),
    path('uvieworders/', views.uvieworders, name="uvieworders"),
    path('postlikes/', views.postlikes, name="postlikes"),
    


    path('searchproducts/', views.searchproducts, name="searchproducts"),
    
    
    

]
