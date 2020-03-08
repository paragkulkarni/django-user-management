from django.db import models

# Create your models here.


class Profile(models.Model):
    owner_image = models.ImageField(
        upload_to='owner_image', blank=True, null=True)
    store_image = models.ImageField(
        upload_to='store_image', blank=True, null=True)
    store_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    registered_number = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.owner_name + ', ' + self.store_name
