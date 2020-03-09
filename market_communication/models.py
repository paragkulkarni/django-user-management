from django.db import models

# Create your models here.


class ProductPost(models.Model):
    information = models.CharField(max_length=400)
    product_image1 = models.ImageField(upload_to='product_image', blank=True)
    product_image2 = models.ImageField(upload_to='product_image', blank=True)
    product_image3 = models.ImageField(upload_to='product_image', blank=True)
    product_image4 = models.ImageField(upload_to='product_image', blank=True)
