from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home_detail/<int:id>', views.home_detail, name='home_detail')
]