from django.urls import path
from property.views import home, home_detail, sign_view, login_view


urlpatterns = [
    path('', home),
    path('home_detail/<int:id>', home_detail, name='home_detail'),
    path('signup/', sign_view, name='sign_view'),
    path('login/', login_view, name='login_view')
]