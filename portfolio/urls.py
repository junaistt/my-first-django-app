# mysite/portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='home_page'), # Homepage for the portfolio app
    path('projects/', views.project_list_view, name='projects_list'),
    path('contact/', views.contact_view, name='contact'),
    # You can remove the old path('home/', views.home, name='home') from previous task if you like
]