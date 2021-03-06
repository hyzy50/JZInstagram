from django.contrib.auth.forms import UserCreationForm

from Insta.models import InstaUser

from django import forms
from django.forms import ModelForm

class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstaUser
        fields = ('username', 'email', 'profile_pic')
