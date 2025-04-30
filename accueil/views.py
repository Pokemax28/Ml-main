

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from produit.models import Produit
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout

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
    users = User.objects.all()
    return render(request, 'accueil/HomePageAdmin.html', {
        'produit_produits': produits,
        'users': users,
        'auth_user': request.user
    })

def HomePageUser(request):
    return render(request, 'accueil/HomePageUser.html', {
        'auth_user': request.user  # On passe juste l'utilisateur authentifié
    })

def RegisterPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return redirect('HomePageUser')  # Redirige vers la page d'accueil utilisateur après l'inscription

    return render(request, 'accueil/RegisterPage.html')


def produit_modifier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    if request.method == 'POST':
        produit.description = request.POST.get('surface')  # ou 'nom', selon ta logique
        produit.prix = request.POST.get('prix')
        produit.save()
        return redirect('HomePageAdmin')  # Remplace par le nom exact de ta page d'accueil admin

    # Si jamais on appelle cette vue en GET, on redirige aussi
    return redirect('HomePageAdmin')


def add_produit(request):
    if request.method == 'POST':
        surface = request.POST.get('surface')
        prix = request.POST.get('prix')
        produit = Produit(surface=surface, prix=prix)
        produit.save()
        return redirect('HomePageAdmin')  # Corrigé ici
    return render('HomePageAdmin.html')


def produit_supprimer(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produit.delete()
    return redirect('HomePageAdmin.html')

def logout_user(request):
    logout(request)
    return redirect('Login')