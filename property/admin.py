from django.contrib import admin
from .models import Property, PropertyImage, PropertyFacility, User, Slider

admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(PropertyFacility)
admin.site.register(User)
admin.site.register(Slider)

