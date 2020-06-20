"""
Views are the functions responsible for managing the display and logic of the
html templates. Views must accept 'request' as their first parameter, but
other parameters can be passed as url logic. Views must return some sort of
response: http, render (an html template with context), or redirect (calling
another view).
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import (
	login,
	logout,
	authenticate,
	update_session_auth_hash
)
from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import quote as to_url
from django.http import HttpResponse, JsonResponse
from .aux_lib import Creature, sort_init_order
from .forms import QuickTrkrForm
from .models import Campaign, UserCampaign, UserCreature, UserItem

# Create your views here.
def homepage(request):
	"""
	Renders the main homepage.
	"""

	return render(
		request,
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
	return render(
		request,
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
	context = {
		'form': form,
		'chars': init_order,
	}
	return render(
		request,
		'main/quick-init-tracker.html',
		context
	)

@login_required
def planner_home(request):
	"""
	Handles displaying the main planner page.
	"""

	def build_campaign_context(campaign_list):
		"""
		Converts the given list of campaigns into a list of tuples to be
		passed to context. Refactored due to repitition.
		"""

		campaign_list = [(c.title, to_url(c.title), c.description)
			if len(c.description) < 150
			else (c.title, to_url(c.title), c.description[:147] + '...')
			for c in campaign_list
		]
		return [(c[0], c[1], c[2])
			if len(c[0]) < 40
			else (c[0][:37] + '...', c[1], c[2])
			for c in campaign_list
		]

	def build_creature_context(creature_list):
		"""
		Converts the given list of creatures into a list of tuples to pass to
		context.
		"""

		creature_list = [(c.name, to_url(c.name), c.description)
			if len(c.description) < 150
			else (c.name, to_url(c.name), c.description[:147] + '...')
			for c in creature_list
		]
		return [(c[0], c[1], c[2])
			if len(c[0]) < 40
			else (c[0][:37] + '...', c[1], c[2])
			for c in creature_list
		]

	def build_item_context(item_list):
		"""
		Converts the given list of creatures into a list of tuples to pass to
		context.
		"""

		item_list = [(i.name, to_url(i.name), i.description)
			if len(i.description) < 150
			else (i.name, to_url(i.name), i.description[:147] + '...')
			for i in item_list
		]
		return [(i[0], i[1], i[2])
			if len(i[0]) < 40
			else (i[0][:37] + '...', i[1], i[2])
			for i in item_list
		]

	# get the user's campaigns
	user_campaigns = [cam.campaign
		for cam in UserCampaign.objects.filter(user=request.user)\
			.order_by('-campaign__last_updated')]
	# split campaigns into most frequently used and least
	top_campaigns = user_campaigns[:4]
	other_campaigns = user_campaigns[4:]

	top_campaigns = build_campaign_context(top_campaigns)
	other_campaigns = build_campaign_context(other_campaigns)

	# get the user's creatures
	user_creatures = [cre.creature
		for cre in UserCreature.objects.filter(user=request.user)\
			.order_by('-creature__last_updated')]
	# split creatures into most frequent and less frequent
	top_creatures = user_creatures[:4]
	other_creatures = user_creatures[4:]

	top_creatures = build_creature_context(top_creatures)
	other_creatures = build_creature_context(other_creatures)

	# get the user's items
	user_items = [item.item
		for item in UserItem.objects.filter(user=request.user)\
			.order_by('-item__last_updated')]
	# split items into most frequent and less frequent
	top_items = user_items[:4]
	other_items = user_items[4:]

	top_items = build_item_context(top_items)
	other_items = build_item_context(other_items)

	context = {
		'top_campaigns': top_campaigns,
		'other_campaigns': other_campaigns,
		'top_creatures': top_creatures,
		'other_creatures': other_creatures,
		'top_items': top_items,
		'other_items': other_items,
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

	context = {
		'initial_title': '',
		'initial_description': '',
	}

	if request.method == 'POST':
		# get the form parameters
		campaign_title = request.POST.get('campaign-title')
		campaign_description = request.POST.get('campaign-description')

		# ensure title is of appropriate length
		if len(campaign_title) > 50:
			messages.error(request, 'Campaign Title must be 50 characters '
				'or less.')
			context['initial_title'] = campaign_title
			context['initial_description'] = campaign_description
			return render(
				request,
				'main/create-campaign.html',
				context
			)

		# create new campaign instance and save
		new_campaign = Campaign()
		new_campaign.title = campaign_title
		new_campaign.description = campaign_description
		new_campaign.save()

		# create new user-campaign mapping and save
		new_user_campaign_mapping = UserCampaign()
		new_user_campaign_mapping.user = request.user
		new_user_campaign_mapping.campaign = new_campaign
		new_user_campaign_mapping.save()

		messages.success(request, 'Successfully created campaign.')
		return redirect('main:planner-home')

	return render(
		request,
		'main/create-campaign.html',
		context
	)

@login_required
def create_creature(request):
	"""

	"""

	context = {}

	return render(
		request,
		'main/create-creature.html',
		context
	)

# ajax views


def ajax_remove_from_init_tracker(request):
	"""
	Handles the removal of a specific character from the intitiative order.
	"""

	target = request.GET.get('target').strip()
	tokens = target.split(' ')
	tokens.pop(0)
	target = ''
	for token in tokens:
		if target != '':
			target += ' ' + token
		else:
			target += token

	found = False

	init_order = request.session['init_order']
	for char in init_order:
		if char['name'] == target:
			found = True
			break

	if found:
		init_order.remove(char)

	request.session['init_order'] = init_order

	return JsonResponse({})
