from django.urls import path
from property.views import home, home_detail, contact_us, about_us

urlpatterns = [
    path('', home, name='home'),
    path('home_detail/<int:id>', home_detail, name='home_detail'),
    path('contact/', contact_us, name='contact_us'),
    path('about/', about_us, name='about_us'),
]