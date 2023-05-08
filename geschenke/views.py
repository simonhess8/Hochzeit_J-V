from django.shortcuts import render
from .models import Geschenk

def home(request):
    geschenkeListe = Geschenk.objects.all()
    return render(request, 'geschenke/home.html', {'geschenkeListe':geschenkeListe})
