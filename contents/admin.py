from django.contrib import admin

# Register your models here.

from .models import Hobby, Description

admin.site.register(Hobby)
admin.site.register(Description)
