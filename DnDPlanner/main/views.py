from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages

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
