from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('logout/', views.logout_request, name='logout'),
	path('login/', views.login_request, name='login'),
	path('init-tracker/', views.init_tracker, name='init-tracker'),
]