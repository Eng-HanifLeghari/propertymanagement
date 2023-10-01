from django import forms
from .models import User, Property


class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    password = forms.PasswordInput()
    image = forms.ImageField()
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'phone_number', 'address', 'title', 'password', 'image']


class PropertyAdminForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PropertyAdminForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].queryset = self.fields['user'].queryset.filter(pk=user.pk)