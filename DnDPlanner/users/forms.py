from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DDPUser

class DDPUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DDPUser
        fields = ('username', 'email')

class DDPUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = DDPUser
        fields = ('username', 'email')
