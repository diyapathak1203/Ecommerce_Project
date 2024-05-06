from django.shortcuts import render
from .models import student
# Create your views here.
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
    return render(request,'shop.html')
def shopping_cart(request):
    return(request,'shopping_cart.html')
def shopd(request):
    return render(request,'shopd.html')
def home(request):
    return render(request,'home.html')
def get_data(request):
    data=student.objects.all()
    print(data)
    context={
        'data':data
    }
    return render(request,'data.html',context)

