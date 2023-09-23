from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    beds = models.CharField(max_length=240, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
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