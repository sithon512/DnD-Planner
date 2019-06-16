from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def homepage(request):
	return render(	request,
					'main/homepage.html',
				)

def login_request(request):
	form = AuthenticationForm()
	return render(	request,
					'main/login.html',
					{'form': form}
				)

def logout_request(request):
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('main:homepage')
