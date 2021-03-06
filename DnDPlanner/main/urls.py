"""
Lists all of the the urls accessible from this app.

Keep the formatting in mind: paths should end with '/' and make sure to
remember the ',' at the end of the line.
"""

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('logout/', views.logout_request, name='logout'),
	path('login/', views.login_request, name='login'),
	path('init-tracker/', views.init_tracker, name='init-tracker'),
	path('planner-home/', views.planner_home, name='planner-home'),
	path('planner-home/new-campaign/', views.create_campaign,
		name='create-campaign'),
	path('planner-home/new-creature/', views.create_creature,
		name='create-creature'),

	# ajax URL's
	path('ajax/rem-char/', views.ajax_remove_from_init_tracker),
]
