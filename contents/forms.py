#craeting forms
from django import forms 
from .models import Hobby, Description

class HobbyForm(forms.ModelForm):
	# inherit from Hobby model
	class Meta:
		model = Hobby
		fields = ['text']
		labels = {'text': ''}

class DescriptionForm(forms.ModelForm):
	# inherit from Description model
	class Meta:
		model = Description
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 150})}