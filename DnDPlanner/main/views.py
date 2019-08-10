"""
Views are the functions responsible for managing the display and logic of the
html templates. Views must accept 'request' as their first parameter, but
other parameters can be passed as url logic. Views must return some sort of
response: http, render (an html template with context), or redirect (calling
another view).
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import QuickTrkrForm
from .aux_lib import Creature, sort_init_order

# Create your views here.
def homepage(request):
	"""
	Renders the main homepage.
	"""

	return render(	request,
					'main/homepage.html',
				)

def login_request(request):
	"""
	Renders the login page. When request method is POST, validates login
	information and authenticates the user.

	Passes the login form to context.
	"""


	if request.user.is_authenticated:
		return redirect('main:homepage')

	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"Logged in user: {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, 'Invalid username or password')

	form = AuthenticationForm()
	return render(	request,
					'main/login.html',
					{'form': form}
				)

@login_required
def logout_request(request):
	"""
	Handles the user clicking "logout" on the navbar from any page. Always
	redirects to the homepage to prevent viewing pages behind a login wall.
	"""

	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('main:homepage')

@login_required
def init_tracker(request):
	"""
	Handles the quick initiative tracker page.

	Passes the character addition form and initiative order to context.
	"""

	if 'init_order' in request.session:
		init_order = request.session['init_order']
	else:
		init_order = []

	if request.method == 'POST':
		print(request.POST)

		if 'add-char' in request.POST:
			form = QuickTrkrForm(request.POST)
			if form.is_valid():
				newChar = Creature(form.cleaned_data.get('character_name'),
					0, # form.cleaned_data.get('character_hp'),
					0, # form.cleaned_data.get('character_ac'),
					form.cleaned_data.get('initiative_roll'),
				)

				if newChar.serialize() not in init_order:
					init_order.append(newChar.serialize())
					init_order = sort_init_order(init_order)
				else:
					messages.error(request, 'That character is already in ' +\
						'the initiative order.')
			else:
				messages.error(request, 'Invalid input.')

		if 'clear-init' in request.POST:
			init_order = []

		# save changes to init order
		request.session['init_order'] = init_order
		return redirect('main:init-tracker')

	form = QuickTrkrForm()
	return render(	request,
					'main/quick-init-tracker.html',
					{'form': form,
					'chars': init_order}
				)

@login_required
def planner_home(request):
	"""
	Handles displaying the main planner page.
	"""

	context = {
		'top_campaigns': range(4),
		'other_campaigns': range(12),
		'top_creatures': range(4),
		'other_creatures': range(40),
		'top_items': range(4),
		'other_items': range(126),
	}	

	return render(
		request,
		'main/planner-home.html',
		context
	)

@login_required
def create_campaign(request):
	"""
	Handles creating a new campaign and adding it to the creating user's
	account. Also renders the creation view.
	"""

	page_title = 'Create Campaign'
	context = {
		'title': page_title,
		'return_target': '/planner-home',
	}

	return render(
		request,
		'main/create-campaign.html',
		context
	)
