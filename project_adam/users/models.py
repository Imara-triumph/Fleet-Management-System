from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
class User(AbstractUser):
    is_driver = models.BooleanField('Is driver', default=False)
    is_fleetowner = models.BooleanField('Is fleetowner', default=False)
    national_id = models.ImageField(blank=True, null=True, upload_to='user_documents/')
    profile_photo = models.ImageField(blank=True, null=True, upload_to='user_documents/')
    driving_license = models.ImageField(blank=True, null=True, upload_to='user_documents/')
    log_book = models.ImageField(blank=True, null=True, upload_to='user_documents/')
    insurance = models.ImageField(blank=True, null=True, upload_to='user_documents/')
    inspection_report = models.ImageField(blank=True, null=True, upload_to='user_documents/', )

    
    groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)


class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=50)
    vehicle_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    chassis_number = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    vehicle_picture = models.ImageField(upload_to='user_documents/')
    # Other fields relevant to the vehicle details

    # You can add more fields as needed based on your requirements

    def __str__(self):
        return f"{self.vehicle_name} - {self.registration_number}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    experience = models.IntegerField()
    # Other fields in your UserProfile model




    

'''class CustomUser(AbstractUser):
    User = get_user_model()
    


    def is_driver(self):
        return self.groups.filter(name='Drivers').exists()

    def is_fleetowner(self):
        return self.groups.filter(name='Fleet Owners').exists()'''

