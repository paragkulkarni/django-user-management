from django.contrib import admin
from .models import ProductPost
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    def admin_image(self, obj):
        return '<img src="%s"/>' % obj.img

    admin_image.allow_tags = True

    list_display = ('information', 'product_image1',
                    'product_image2', 'product_image3', 'product_image4')


admin.site.register(ProductPost, ProductAdmin)
