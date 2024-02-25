from django.urls import path

from . import views



urlpatterns = [

    path('', views.all_products, name='all_products'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category_list/<slug:category_slug>/', views.category_list, name='category_list'),
    path('store/', views.store, name='my-store'),
    

]