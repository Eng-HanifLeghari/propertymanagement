from django.contrib import admin
from .models import Property, PropertyImage, PropertyFacility, User, Slider

# admin.site.register(Property)
# admin.site.register(PropertyImage)
admin.site.register(PropertyFacility)
admin.site.register(User)
admin.site.register(Slider)


class PropertyImageInline(admin.TabularInline):  # You can use `admin.StackedInline` for a different display style
    model = PropertyImage
    display = ['description']
    extra = 0
    max_num = 1


@admin.register(Property)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]