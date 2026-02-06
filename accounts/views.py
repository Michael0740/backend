from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register(request):
    return HttpResponse("Register Page")

def login_view(request):
    return HttpResponse("Login Page")

def logout_view(request):
    return HttpResponse("Logout Page")
