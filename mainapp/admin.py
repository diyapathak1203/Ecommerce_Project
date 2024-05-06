from django.contrib import admin
from  .models import *
# Register your models here.
# admin.site.register(student)
@admin.register(student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','address','mob','roll','image','file']