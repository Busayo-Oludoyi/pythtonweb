from django.urls import path
from .import views

urlpatterns = [
    path('', views.main,  name='main'),
    path('members/', views.members, name='members'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
