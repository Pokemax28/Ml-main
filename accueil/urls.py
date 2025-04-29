"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.urls import include
from django.conf import settings

urlpatterns = [
   path('', views.index, name='Login'),
   path('HomePageAdmin/', views.HomePageAdmin, name='HomePageAdmin'),
       path('RegisterPage/', views.RegisterPage, name='RegisterPage'),
    path('HomePageUser/', views.HomePageUser, name='HomePageUser'),
   path('produit_supprimer/<int:produit_id>/', views.produit_supprimer, name='produit_supprimer'),
  path('produit_modifier/<int:produit_id>/', views.produit_modifier, name='produit_modifier'),
  path('produit_add_admin/', views.add_produit, name='produit_add_admin'),
  path('produit/', include('produit.urls')),


]

