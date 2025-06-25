from django.contrib import admin

# Register your models here.
# mysite/portfolio/admin.py
from django.contrib import admin
from .models import Project, ContactMessage # Import your models

admin.site.register(Project)
admin.site.register(ContactMessage)