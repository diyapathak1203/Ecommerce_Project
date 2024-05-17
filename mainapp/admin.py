from django.contrib import admin
from  .models import *
# Register your models here.
# admin.site.register(student)
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','description','product_image','category','size']


admin.site.register(AddCart)