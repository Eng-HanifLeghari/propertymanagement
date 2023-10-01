from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Property, PropertyImage, Slider, PropertyFacility
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from property.models import User


def home(request):
    slider = Slider.objects.all()
    queryset = Property.objects.all()
    propertyimage = PropertyImage.objects.all()
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page', 1)

    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {
        'queryset': page_obj,
        'slider': slider,
        'propertyimage': propertyimage
    }
    return render(request, 'property/index.html', context)


def home_detail(request, id):
    try:
        get_data_by_user = Property.objects.get(id=id)
    except Property.DoesNotExist:
        get_data_by_user = None
    try:
        amenities = PropertyFacility.objects.get(property_id=id)
        amenities = amenities.amanities_detail()
    except PropertyFacility.DoesNotExist:
        amenities = None
    try:
        user_agents = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        user_agents = None
    context = {
        'get_data_by_user': get_data_by_user,
        'amenities': amenities,
        'user_agents': user_agents
    }
    return render(request, 'property/detail.html', context)


def contact_us(request):
    return render(request, 'property/contact.html')


def about_us(request):
    return render(request, 'property/about.html')