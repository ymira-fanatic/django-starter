from django.shortcuts import render
from.models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Tech City'
    dest2.price = 800

    dest3 = Destination()
    dest3.name = 'Kolkata'
    dest3.desc = 'City of Joy'
    dest3.price = 900

    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests': dests})
