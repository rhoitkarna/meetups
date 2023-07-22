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


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first Meetup'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
