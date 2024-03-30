from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.models import CartItem, Cart
from cart.views import _cart_id
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from django.db.models import Q
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
    product = get_object_or_404(Product.objects.filter(slug=slug, in_stock=True)[:1])
    # if it is in cart 
    in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product=product).exists()

    context = {'product':product, 'in_cart':in_cart}
    return render(request, 'app/product/product_detail.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category, in_stock=True)
    paginator = Paginator(product, 2)
    page = request.GET.get('page')
    page = request.GET.get('page')
    page_product = paginator.get_page(page)

    product_count = product.count()
    context= {'products':page_product, 'category':category, 'product_count':product_count}
    # return render(request, 'app/product/category.html', context)
    return render(request, 'app/store/store.html', context)

def store(request):
    products = Product.objects.all().filter(in_stock=True)
    #paginator
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    page_product = paginator.get_page(page)

    product_count = products.count()

    context = {'products':page_product, 'product_count':product_count,'page_product':page_product}
    return render(request, 'app/store/store.html', context)

def search(request):
    products = None  # Define product outside the if blocks

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created').filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))
            product_count = products.count()
        else:
            products = Product.objects.none()
    context = {'products': products, 
               'product_count':product_count}
    return render(request, 'app/store/store.html', context)