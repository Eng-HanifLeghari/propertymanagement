from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from property.models import Property, PropertyFacility, PropertyImage


def sign_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone_number = request.POST.get("number")
        title = request.POST.get("title")
        password = request.POST.get("password")
        password_retype = request.POST.get("password_retype")
        image = request.POST.get("image")

        # Check if a user with the same email or username already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "A user with the same username or email already exists.")
            return render(request, 'accounts/sign_up.html')

        if password != password_retype:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/sign_up.html')
        user = User(username=username, email=email, address=address, phone_number=phone_number, title=title,
                    image=image, is_staff=True)
        user.set_password(password)
        user.save()


            # Add the user to the 'developers' group (if it doesn't exist, create it)
        group, created = Group.objects.get_or_create(name="Noam")
        if created:
            property_content_type = ContentType.objects.get_for_model(Property)
            facility_content_type = ContentType.objects.get_for_model(PropertyFacility)
            image_content_type = ContentType.objects.get_for_model(PropertyImage)

            group.permissions.add(
                Permission.objects.get(content_type=property_content_type, codename="add_property"),
                Permission.objects.get(content_type=property_content_type, codename="change_property"),
                Permission.objects.get(content_type=property_content_type, codename="delete_property"),
                # Add other Property permissions as needed
            )

            # Add permissions for the PropertyFacility model
            group.permissions.add(
                Permission.objects.get(content_type=facility_content_type, codename="add_propertyfacility"),
                Permission.objects.get(content_type=facility_content_type, codename="change_propertyfacility"),
                Permission.objects.get(content_type=facility_content_type, codename="delete_propertyfacility"),
                # Add other PropertyFacility permissions as needed
            )

            # Add permissions for the PropertyImage model
            group.permissions.add(
                Permission.objects.get(content_type=image_content_type, codename="add_propertyimage"),
                Permission.objects.get(content_type=image_content_type, codename="change_propertyimage"),
                Permission.objects.get(content_type=image_content_type, codename="delete_propertyimage"),
                # Add other PropertyImage permissions as needed
            )
        group.user_set.add(user)

        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login_view')

    return render(request, 'accounts/sign_up.html')


# @login_required
def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('admin:index')

    return render(request, 'accounts/login.html')


def sign_out(request):
    # Log the user out
    logout(request)

    # Display a success message
    messages.success(request, 'Logged out successfully!')

    # Redirect the user to the home page
    return redirect('login_view')