# Defining urls for users
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	# Registration ulr
	path('register/', views.register, name='register'), 
]