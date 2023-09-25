from django.shortcuts import render
from .models import Property, PropertyImage, Slider


def home(request):
    slider = Slider.objects.all()
    queryset = Property.objects.all()
    propertyimage = PropertyImage.objects.all()
    context = {
        'queryset': queryset,
        'slider': slider,
        'propertyimage': propertyimage
    }
    return render(request, 'property/index.html', context)


def home_detail(request, id):
    get_data_by_user = Property.objects.get(id=id)
    context = {
        'get_data_by_user': get_data_by_user
    }
    return render(request, 'property/detail.html', context)