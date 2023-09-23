from django.shortcuts import render
from .models import Property


def home(request):
    queryset = Property.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'property/index.html', context)


def home_detail(request, id):
    get_data_by_user = Property.objects.get(id=id)
    context = {
        'get_data_by_user': get_data_by_user
    }
    return render(request, 'property/detail.html', context)