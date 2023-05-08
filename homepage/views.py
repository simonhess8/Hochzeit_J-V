from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.http import Http404

def home(request):
    return render(request, 'homepage/home.html')

def galerie(request):
    return render(request, 'homepage/galerie.html')

def rückmeldung(request):
    user = request.user
    if request.user.is_authenticated and request.method == 'GET':
        user.profile.status = request.GET.get('status', user.profile.status)
        user.profile.anzahlPersonenAlt = request.GET.get('anzahlAlt', user.profile.anzahlPersonenAlt)
        user.profile.anzahlPersonenJung = request.GET.get('anzahlJung', user.profile.anzahlPersonenJung)
        user.save() 
        return render(request, 'homepage/rückmeldung.html') 
    else:
        return render(request, 'homepage/rückmeldung.html')        

def infos(request):
    return render(request, 'homepage/infos.html')

def signupuser(request):
    
    if request.method == 'GET':
        return render(request, 'homepage/signupuser.html', {'form': UserCreationForm()})
    else:
        #create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'homepage/signupuser.html', {'form': UserCreationForm(), 'error':'Der Benutzername ist schon vergeben, bitte wähle einen anderen oder melde dich an'})

        else:
            return render(request, 'homepage/signupuser.html', {'form': UserCreationForm(), 'error':'Da haben die Passwörter leider nicht übereingestimmt...'})
            #error that the passwords didn't match


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'homepage/loginuser.html', {'form': AuthenticationForm()})
    else:
       user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       if user == None:
           return render(request, 'homepage/loginuser.html', {'form': AuthenticationForm(), 'error':'Benutzername und Passwort haben nicht gepasst'})
       else:
            login(request, user)
            return redirect('home')
def home(request):
    return render(request, 'homepage/home.html')