from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddToInitTrkrForm
from .aux_lib import Creature, sort_init_order

# Create your views here.
def homepage(request):
	return render(	request,
					'main/homepage.html',
				)

def login_request(request):
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

def logout_request(request):
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('main:homepage')

def init_tracker(request):
	if 'init_order' in request.session:
		init_order = request.session['init_order']
	else:
		init_order = []

	if request.method == 'POST':
		print(request.POST)

		if 'add-char' in request.POST:
			form = AddToInitTrkrForm(request.POST)
			if form.is_valid():
				newChar = Creature(form.cleaned_data.get('character_name'),
					0, # form.cleaned_data.get('character_hp'),
					0, # form.cleaned_data.get('character_ac'),
					form.cleaned_data.get('initiative_roll'),
				)

				if newChar.serialize() not in init_order:
					init_order.append(newChar.serialize())
					# BOOKMARK: need to sort by initiative_roll
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

	form = AddToInitTrkrForm()
	return render(	request,
					'main/quick-init-tracker.html',
					{'form': form,
					'chars': init_order}
				)
