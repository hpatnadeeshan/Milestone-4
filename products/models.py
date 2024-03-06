from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255)
    sku = models.IntegerField()
    gtin12 = models.BigIntegerField(null=True, blank=True)
    breadcrumb = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    availability = models.CharField(max_length=50)
    image_url = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    reviews_count = models.IntegerField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    calory_content = models.CharField(max_length=100,null=True, blank=True)
    nutrition_analysis = models.TextField(null=True, blank=True)
    feeding_instructions = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.name