# Create your views here.
from django.shortcuts import render
from .models import Produit
from .ml.predictor import predict_price

def index(request):
    produits = Produit.objects.all()
    return render(request, 'produit/index.html',{'produits':produits})



def prediction_view(request):
    result = None
    if request.method == 'POST':
        surface = request.POST.get('surface')
        if surface:
            result = predict_price(surface)
    return render(request, 'produit/predict.html', {'result': result})
