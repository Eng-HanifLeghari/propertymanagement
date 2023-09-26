from django.shortcuts import render
from .models import Property, PropertyImage, Slider, PropertyFacility
from .forms import UserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    get_data_by_user = Property.objects.get(id=id)
    amenities = PropertyFacility.objects.get(id=id)
    context = {
        'get_data_by_user': get_data_by_user,
        'amenities': amenities
    }
    return render(request, 'property/detail.html', context)


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserForm()
    return render(request, 'accounts/sign_up.html', {'form': form})
