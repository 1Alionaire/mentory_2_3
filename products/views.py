from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from products.models import Product, ProductCategory
from products.forms import InputProductForm
from datetime import datetime
# Create your views here.

def return_main_page(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/index.html', context)

def add_products(request):
    if request.method == 'POST':
        form = InputProductForm(request.POST)
        if form.is_valid():
            need_data = form.save(commit=False)
            need_data.dateAdded = datetime.now()
            form.save()
            return HttpResponseRedirect('/')
        else:
            print('form not valid')
    else:
        form = InputProductForm()
    context = {'form':form,
               'categories': ProductCategory.objects.all()}
    return render(request, 'products/add_products.html', context)

def edit_product(request, id):
    try:
        chosen_product = Product.objects.get(id=id)
        if request.method == 'POST':
            chosen_product.name = request.POST.get('name')
            chosen_product.description = request.POST.get('description')
            need_category = request.POST.get('category')
            need_category_id = ProductCategory.objects.get(id=int(need_category[8]))
            chosen_product.category = need_category_id
            chosen_product.price = request.POST.get('price')
            chosen_product.quantity = request.POST.get('quantity')
            chosen_product.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'products/edit_product.html', context={
                'chosen_product': chosen_product,
                'categories': ProductCategory.objects.all()
            })
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')

def delete_product(request, id):
    try:
        chosen_product = Product.objects.get(id=id)
        chosen_product.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')

def product_list(request, id):
    products = Product.objects.all()
    need_category = ProductCategory.objects.get(id=id)
    if id:
        products = products.filter(category=need_category)
    context = {
        'title': 'Store - Каталог',
        'products': products,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/product_list.html', context=context)

def product_search(request):
    query = request.POST.get('form_search')
    print(query)
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    context = {
        'title': 'Store - Каталог',
        'products': products,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/search_list.html', context=context)