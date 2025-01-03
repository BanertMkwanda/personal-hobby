from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Hobby(models.Model):
	# User's hobby
	text = models.CharField(max_length=20)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	class Meta:
		verbose_name_plural = 'hobbies'

	def __str__(self):
		# return string representation of the model.
		return self.text

class Description(models.Model):
	hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
	text = models.TextField()	
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'descriptions'

	def __str__(self):
		# return string representation of the model.
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
		else:
			return self.text		
