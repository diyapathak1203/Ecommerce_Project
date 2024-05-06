from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    address=models.TextField(max_length=200)
    mob=models.CharField(max_length=10)
    image=models.ImageField(upload_to='images')
    file=models.FileField()