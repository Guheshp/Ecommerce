from django.db import models


from django.urls import reverse
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'product_creater', on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True)
    slug = models.SlugField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(null=True)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def __str__(self):
        return self.title
