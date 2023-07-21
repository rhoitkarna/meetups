from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'location': 'Kathmandu',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Second Meetup',
            'location': 'Pokhara',
            'slug': 'a-second-meetup'
        }]
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })
