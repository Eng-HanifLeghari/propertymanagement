from django.db import models
from django.contrib.auth.models import AbstractUser


class Slider(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class User(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    password_retype = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_property')
    title = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    beds = models.CharField(max_length=240, null=True, blank=True)
    bathroom = models.CharField(max_length=60, null=True, blank=True)
    house_size = models.CharField(max_length=50, null=True, blank=True)
    garage = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    for_rent_or_sale = models.CharField(max_length=50, null=True, blank=True)
    feature = models.CharField(max_length=60, null=True, blank=True)
    property_type_family_or_bachelor = models.CharField(max_length=70, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    property_ID = models.CharField(max_length=30, null=True, blank=True)
    property_Type = models.CharField(max_length=50, null=True, blank=True)
    property_Status = models.CharField(max_length=70, null=True, blank=True)
    rooms = models.CharField(max_length=50, null=True, blank=True)
    year_built = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_image')
    description = models.CharField(max_length=80, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.description


class PropertyFacility(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_facility')
    air_cond = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    dishwasher = models.BooleanField(default=False)
    bedding = models.BooleanField(default=False)
    cable_tv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)

    def __str__(self):
        return self.property.title

