from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class student(models.Model):
#     name=models.CharField(max_length=50)
#     roll=models.IntegerField()
#     address=models.TextField(max_length=200)
#     mob=models.CharField(max_length=10)
#     image=models.ImageField(upload_to='images')
#     file=models.FileField()

category=[
        ("Men","men"),
        ("Women","women"),
        ("Kids","kids"),
        ("Best","best"), 
    ]
class Product(models.Model):
        title=models.CharField(max_length=50)
        price=models.IntegerField()
        description=models.CharField(max_length=200)
        product_image=models.ImageField(upload_to='media')
        category=models.CharField(choices=category,max_length=50,null=True,blank=True)
        size=models.CharField(max_length=20,null=True,blank=True)
class AddCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(max_length = 50)

