

# Create your views here.
from django.shortcuts import render
from .models import Activite

def index(request):
    activites = Activite.objects.all()
    return render(request, 'indexo.html',{'activites':activites})
