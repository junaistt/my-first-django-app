# mysite/portfolio/views.py
from django.shortcuts import render, redirect # Import redirect
from django.urls import reverse # Import reverse
from .models import Project, ContactMessage

def homepage_view(request):
    return render(request, 'portfolio/homepage.html')

def project_list_view(request):
    projects = Project.objects.all().order_by('-date_created')
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/project_list.html', context)

def contact_view(request):
    if request.method == 'POST':
        # Get data from the submitted form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', '') # Subject is optional, provide default empty string
        message = request.POST.get('message')

        # Basic Validation (you'll learn more advanced validation later with Django Forms)
        if name and email and message: # Check if essential fields are not empty
            # Save to database using ORM
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            # Redirect to a 'thank you' page or back to the contact page with a success message
            # For now, let's redirect to home_page for simplicity, or we can make a dedicated success page
            # We'll use Django messages framework later for actual messages
            return redirect(reverse('home_page'))
        else:
            # If validation fails, re-render the form with an error message (for now, simple print)
            print("Error: Please fill in all required fields (Name, Email, Message).")
            # You might want to pass an error message to the template here
            context = {
                'error_message': "Please fill in all required fields (Name, Email, Message)."
            }
            return render(request, 'portfolio/contact_form.html', context)
    else: # If it's a GET request, just display the empty form
        return render(request, 'portfolio/contact_form.html')