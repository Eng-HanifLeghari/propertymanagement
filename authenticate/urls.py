from django.urls import path
from authenticate.views import sign_view, login_view, sign_out


urlpatterns = [
        path('signup/', sign_view, name='sign_view'),
        path('login/', login_view, name='login_view'),
        path('signout/', sign_out, name='logout_view'),
    ]