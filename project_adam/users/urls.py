from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', views.admin, name= 'admin'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path("driver", views.driver, name="driver"),
    path("fleetowner", views.fleetowner, name="fleetowner"),
    path("register_upload", views.register_upload, name="register_upload"),
    path('upload/', views.upload_document, name='upload_document'),
    path('profile', views.profile, name='profile'),
    path('add', views.add, name='add'),
    

]