from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
	if request.method != 'POST':
		# Data entered; send form
		form = UserCreationForm()
	else:
		# Data subnitted; process form
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.save()
			# login user
			login(request, new_user)
			return redirect('contents:index')

	context = {'form': form}
	return render(request, 'registration/register.html', context)

