from django.db import models

# Create your models here.
# mysite/portfolio/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(blank=True, null=True) # URL to an image
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True) # Automatically set when created

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField() # Specific field for email
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True) # Automatically set when created
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject[:50]}..." # Show subject snippet