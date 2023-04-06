"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: Cime(cime.pro@gmail.com) 
views.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  mardi 14 mars 2023, 23:37:54 
Dernière modification : mercredi 15 mars 2023, 1:11:50
"""
from django.shortcuts import render
from .models import *
from django.contrib import messages
from geopy.geocoders import Nominatim


def home(request):
    bio=biomasse.objects.all()
    try : 
        if request.method == 'POST':
            Localité = request.POST.get("localité")
            Type = request.POST.get("type")
            geolocator = Nominatim(user_agent="home")
            location = geolocator.geocode(Localité+" Togo")
            latitude = location.latitude
            longitude = location.longitude
            Localisation = str(latitude)+","+str(longitude)
            b=biomasse.objects.create(Localité=Localité,Localisation=Localisation,Type=Type)
            b.save()
            
            messages.warning(request,'Enrégistrer') 
            return render(request, "home.html", {"b":bio})
        else :
            return render(request, "home.html",{"b":bio})
    except:
        messages.warning(request,'Adresse Introuvable') 
        return render(request, "home.html", {"b":bio})