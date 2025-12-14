from django.shortcuts import render, redirect

# Create your views here.
from .models import Hobby, Description
from .forms import HobbyForm, DescriptionForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import JsonResponse
from .matches import my_list

def match(request):
    return JsonResponse(my_list, safe=False)

def index(request):
	# Home page
	return render(request, 'contents/index.html')

@login_required
def hobbies(request):
	# hobbies page
	hobbies = Hobby.objects.filter(owner=request.user).order_by('date_added')
	context = {'hobbies': hobbies}

	return render(request, 'contents/hobbies.html', context)

@login_required
def hobby(request, hobby_id):
	# Displaying each hobby and it's entries on separate page.
	hobby = Hobby.objects.get(id=hobby_id)
	# make sure descriptions that belong to them.
	if hobby.owner != request.user:
		raise Http404

	descriptions = hobby.description_set.order_by('-date_added')

	context = {'hobby': hobby, 'descriptions': descriptions}
	return render(request, 'contents/hobby.html', context)

@login_required
def new_hobby(request):
	if request.method != 'POST':
		# No data submitted; create blank form
		form = HobbyForm()
	else:
		# Data submitted; process form
		form = HobbyForm(data=request.POST)
		if form.is_valid():
			new_hobby = form.save(commit=False)
			new_hobby.owner =request.user
			new_hobby.save()
			# Redirecr user hobbies list page
			return redirect('contents:hobbies')

	context = {'form': form}
	return render(request, 'contents/new_hobby.html', context)

@login_required
def new_description(request, hobby_id):
	hobby = Hobby.objects.get(id=hobby_id)

	# make sure descriptions that belong to them.
	if hobby.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# No data submitted; create blank form
		form = DescriptionForm()
	else:
		# Data submitted;process form
		form = DescriptionForm(data=request.POST)
		if form.is_valid():
			new_description = form.save(commit=False)
			new_description.hobby = hobby
			new_description.save()
			# Redirect user to hobby page to see descriptions available
			return redirect('contents:hobby', hobby_id=hobby_id)

	context = {'hobby': hobby, 'form': form}
	return render(request, 'contents/new_description.html', context)

@login_required
def edit_hobby(request, hobby_id):
	hobby = Hobby.objects.get(id=hobby_id)
	# make sure descriptions that belong to them.
	if hobby.owner != request.user:
		raise Http404
	
	if request.method != 'POST':
		# No data edited; send form to be edited.
		form = HobbyForm(instance=hobby)
	else:
		# Data edited; process form
		form = HobbyForm(instance=hobby, data=request.POST)
		if form.is_valid():
			form.save()	
			# return the user to the hobbies page to see available hobbies
			return redirect('contents:hobbies')

	context = {'hobby': hobby, 'form': form}	
	return render(request, 'contents/edit_hobby.html', context)	

@login_required
def edit_description(request, description_id):
	description = Description.objects.get(id=description_id)
	hobby = description.hobby
	# make sure descriptions that belong to them.
	if hobby.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# No data edited; send form to be edited.
		form = DescriptionForm(instance=description)
	else:
		# Data edited; process form
		form = DescriptionForm(instance=description, data=request.POST)
		if form.is_valid():
			form.save()	
			# return the user to the hobbies page to see available hobbies
			return redirect('contents:hobby', hobby.id )

	context = {'hobby': hobby, 'description': description, 'form': form}	
	return render(request, 'contents/edit_description.html', context)	















































