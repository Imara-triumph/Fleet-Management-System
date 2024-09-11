from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



def index(request):
    return render(request, "mamba/index.html")


def requirements(request):
    return render(request,"mamba/requirements.html")


def about(request):
    return render(request,"mamba/about.html")


def privacy(request):
    return render(request,"mamba/privacy.html")
    



    