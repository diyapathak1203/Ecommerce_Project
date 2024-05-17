from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.`
def index(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html')
def blogd(request):
    return render(request,"blogd.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def shop(request):
    data=Product.objects.all()
    context={
        'data':data
    }
    return render(request,'shop.html',context)
def shopping_cart(request):
    return(request,'shopping_cart.html')
def shopd(request,id):
    data=Product.objects.get(id=id)
    print(data,"<<<data>>>>")
    context={
        'data':data
    }
    return render(request,'shopd.html',context)
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == "POST":
        uname = request.POST['username']
        uemail = request.POST['email']
        upassword = request.POST['password']
        upassword1 = request.POST['password1']
        
        user = User(username=uname,email=uemail)
        
        if User.objects.filter(username=uname).first():
            messages.success(request,'Username already exits!!!')
        elif upassword==upassword1:
          user.set_password(upassword)
          user.save()
          messages.success(request,'User account successfully created !!!')
        else:
            messages.success(request,"password field not match !!!")
        
    return render(request,'signup.html')

def loginhandle(request):
    if request.method == "POST":
        uname = request.POST["username"]
        upassw = request.POST["password"]
        
        user_obj = User.objects.filter(username=uname).first()
        user = authenticate(username=uname,password=upassw)
        if user_obj is None:
            messages.success(request,'user not found !!!')
        
        if user is None:
            messages.success(request,'Wrong Password !!')
        
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')

def logouthandle(request):
    logout(request)
    return redirect('/')

def addtocart(request):
    if request.method == "POST":
        user = request.user 
        prod_id = request.POST['prod_id']
        product = Product.objects.get(id=prod_id)
        size = request.POST['size']
        quantity = request.POST['quantity']
        # print(size,"size>><<<")
        AddCart(user=user,product=product,size=size,quantity=quantity).save()
        return redirect('/addtocart/')
    else:
        data = AddCart.objects.filter(user=request.user)
        for i in data:
            i.total_price = i.product.price * i.quantity
        context = {
            'data':data,
        }
        return render(request,'shopping_cart.html',context)

def cart_product_delete(request,id):
    cart_product = AddCart.objects.filter(id=id)
    cart_product.delete()
    return redirect('/addtocart/')



