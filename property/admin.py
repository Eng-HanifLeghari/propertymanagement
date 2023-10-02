from django.contrib import admin
from .models import Property, PropertyImage, PropertyFacility, User, Slider
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
        list_display = ('username', 'email', 'image', 'address', 'phone_number', 'title', 'is_staff', 'is_active')
        list_filter = ('is_staff', 'is_active')
        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal Info', {'fields': ('username',)}),  # Corrected 'username' field definition
            ('Permissions', {'fields': ('is_staff', 'is_active')}),
        )
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            }),
        )
        search_fields = ('email', 'username')
        ordering = ('email',)


admin.site.register(PropertyFacility)
# admin.site.register(User)
admin.site.register(Slider)


class PropertyImageInline(admin.TabularInline):  # You can use `admin.StackedInline` for a different display style
    model = PropertyImage
    display = ['description']
    extra = 0
    max_num = 20


class PropertyFacilityInline(admin.TabularInline):  # You can use `admin.StackedInline` for a different display style
    model = PropertyFacility
    display = ['air_cond']
    extra = 0
    max_num = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'user')
    list_filter = ('for_rent_or_sale', 'property_Type', 'property_Status')
    search_fields = ('title', 'location')
    inlines = [PropertyImageInline, PropertyFacilityInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Check if the user is a superuser, and if so, return all data
        if request.user.is_superuser:
            return qs

        # If the user is staff (but not a superuser), limit the data they can see
        return qs.filter(user=request.user)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(
            request, queryset, search_term)

        # Filter the queryset to only include the properties of the logged-in user
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)

        return queryset, use_distinct

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":  # Replace "user" with the actual name of your ForeignKey field
            if request.user.is_superuser:
                # Superadmins can see all users
                kwargs["queryset"] = User.objects.all()
            else:
                # Staff users can only see themselves
                kwargs["queryset"] = User.objects.filter(id=request.user.id)
        # return super().formfield_for
        return super().formfield_for_foreignkey(db_field, request, **kwargs)