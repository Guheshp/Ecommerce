from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def categories(request):
    return{
        'categories':Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all().filter(in_stock=True)
    context = {'products':products}
    return render(request, 'app/home.html', context) #render is used to loading templates


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {'product':product}
    return render(request, 'app/product/product_detail.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category, in_stock=True)
    product_count = product.count()
    context= {'products':product, 'category':category, 'product_count':product_count}
    # return render(request, 'app/product/category.html', context)
    return render(request, 'app/store/store.html', context)

def store(request):
    products = Product.objects.all().filter(in_stock=True)
    product_count = products.count()

    context = {'products':products, 'product_count':product_count}
    return render(request, 'app/store/store.html', context)