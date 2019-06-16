from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def homepage(request):
	messages.success(request, 'messages working')
	return render(	request,
					"main/homepage.html",
				)

def login_request(request):
	pass

def logout_request(request):
	pass
