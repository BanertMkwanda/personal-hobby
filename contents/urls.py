# Defining urls for contents

from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
 path('matches/', views.matches, name="matches"),
	# home page url
	path('', views.index, name='index'),
	# Hobbies page
	path('hobbies/', views.hobbies, name='hobbies'),
	# Hobby page displaying it's description
	path('hobby/<int:hobby_id>/', views.hobby, name='hobby'),
	# Adding new hobby
	path('new_hobby/', views.new_hobby, name='new_hobby'),
	# Adding new description
	path('new_description/<int:hobby_id>/', views.new_description, name='new_description'),
	#editting hobby
	path('edit_hobby/<int:hobby_id>/', views.edit_hobby, name='edit_hobby'),
	# editting description
	path('edit_description/<int:description_id>/', views.edit_description, name='edit_description'),
]