from django.db import models

# Create your models here.
# blog/models.py
from django.db import models

class Produit(models.Model):
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    

class Prediction(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    date_prediction = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Prediction for {self.produit} on {self.date_prediction}"