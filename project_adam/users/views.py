from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.db import IntegrityError
from .forms import VehicleForm
# Create your views here.




def add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
           
            form.save() 
            return HttpResponseRedirect('users/fleetowner.html')  # Change the URL to your desired URL

    else:
        form = VehicleForm()

    return render(request, 'users/add.html', {'form': form})


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user = form.save()
            
            if form.cleaned_data['is_driver']:
                group_name = 'Drivers'
            else:
                group_name = 'Owners'

            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            msg = 'user created'
            return redirect('user_login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'users/register.html', {'form': form, 'msg': msg})


def user_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_driver:
                login(request, user)
                return redirect('driver')
            elif user is not None and user.is_fleetowner:
                login(request, user)
                return redirect('fleetowner')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'users/login.html', {'form': form, 'msg': msg})


def user_logout(request):
    logout(request)
    return render(request, "mamba/index.html" )



def driver(request):
   return render(request,'users/driver.html')


def fleetowner(request):
    return render(request,'users/fleetowner.html')




def register_upload(request):
    return render(request, 'users/register_upload.html', {'content_type': request.GET.get('content_type', '')})




def upload_document(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and associate it with the logged-in user
            user = request.user
            user.profile_photo = form.cleaned_data['profile_photo']
            user.save()
            return redirect('users/register_upload.html',{'scroll_to': '#welcome_reg'})  # Redirect to a success page or another URL
    else:
        form = UserForm()
    
    return render(request, 'users/register_upload.html', {'form': form, 'scroll_to': '#welcome_reg'})


def profile(request):
    return render(request, 'users/profile.html')

def add(request):
    return render(request, 'users/add.html')
