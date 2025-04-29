

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from produit.models import Produit
from django.shortcuts import get_object_or_404

#from .models import Article

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.is_staff:
                return redirect('HomePageAdmin')
            else:
                return redirect('HomePageUser')
        else:
            return render(request, 'accueil/index.html', {'error': 'Invalid credentials'})
    
    return render(request, 'accueil/index.html')



def HomePageAdmin(request):
    produits = Produit.objects.all()
    return render(request, 'accueil/HomePageAdmin.html', {
        'produit_produits': produits,
        'auth_user': request.user
    })

def HomePageUser(request):
   produits = Produit.objects.all()
   return render(request, 'accueil/HomePageUser.html', {
        'produit_produits': produits,
        'auth_user': request.user  # pour {{ auth_user.username }}
    })


def RegisterPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return redirect('index')

    return render(request, 'accueil/RegisterPage.html')

def produit_modifier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    
    if request.method == 'POST':
        # Récupérer les nouvelles données
        produit.surface = request.POST['surface']
        produit.prix = request.POST['prix']
        produit.save()

        return redirect('HomePageAdmin')  # Redirige vers la page d'accueil après modification

    return redirect('/accueil/HomePageAdmin.html')

def produit_supprimer(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produit.delete()
    return redirect('/accueil/HomePageAdmin.html')
    