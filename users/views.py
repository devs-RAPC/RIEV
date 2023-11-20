from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def logout_view(request):
    """Faz o logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))
