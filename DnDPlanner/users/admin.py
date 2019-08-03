from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import DDPUserCreationForm, DDPUserChangeForm
from .models import DDPUser

class DDPUserAdmin(UserAdmin):
    add_form = DDPUserCreationForm
    form = DDPUserChangeForm
    model = DDPUser
    list_display = ['email', 'username', 'is_staff']

admin.site.register(DDPUser, DDPUserAdmin)
