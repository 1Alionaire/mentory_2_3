"""
URL configuration for super project.

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
from django.urls import path, include
from products.views import return_main_page, add_products, edit_product, delete_product, product_list, product_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_products', add_products, name = 'add_products'),
    path('edit_product/<int:id>/', edit_product, name = 'edit_product'),
    path('', return_main_page, name = 'return_main_page'),
    path('product_list/<int:id>/', product_list, name = 'product_list'),
    path('product_search/', product_search, name = 'product_search'),
    path('delete_product/<int:id>/', delete_product, name = 'delete_product'),
]
