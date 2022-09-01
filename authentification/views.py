from django.shortcuts import render
from django.contrib.auth.views import LoginView
from authentification.forms import EmailAuthenticationForm
# Create your views here.
class EmailLoginView(LoginView):
    '''validate user with Email'''
    authentication_form =  EmailAuthenticationForm
