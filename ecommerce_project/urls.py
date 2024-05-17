"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('blog/',views.blog),
    path('blogd/',views.blogd),
    path('contact/',views.contact),
    path('shop/',views.shop),
    path('shopd/<int:id>/',views.shopd),
    path('shopping_cart/',views.shopping_cart),
    path('about/',views.about),
    path('',views.home),
    path('signup/',views.signup),
    path('login/',views.loginhandle),
    path('logout/',views.logouthandle),
    path('addtocart/',views.addtocart),
    path('cart_product_delete/<int:id>/',views.cart_product_delete)


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
