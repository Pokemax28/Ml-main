from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from .models import Article

def index(request):
    #articles = Article.objects.all()
    return render(request, 'accueil/index.html')


def login(request):
    return render(request, 'accueil/login.html')
