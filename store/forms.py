from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Customer

class createUserForm(UserCreationForm):
    # email = forms.EmailField(label=("Email address"))
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class customerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']    
        labels = {
                "name": _("Name     "),
                "email": _("Email Address"),
                }