from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Vehicle

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ) 
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta  :
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_driver', 'is_fleetowner')


class UserForm(forms.ModelForm):
    class Meta:
        model = User  # Use your User model
        fields = ['national_id', 'profile_photo', 'driving_license', 'log_book', 'insurance', 'inspection_report']    


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle 
        fields = ['registration_number', 'vehicle_name', 'model', 'chassis_number', 'price', 'vehicle_type', 'vehicle_picture']