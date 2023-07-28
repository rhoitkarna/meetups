from django.urls import path
from . import views

urlpatterns = [
    path('<slug:meetup_slug>/register', views.registration, name='registration'),
    path('', views.index, name='index'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-details'),
]
