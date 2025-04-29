from django.db import models

# Create your models here.
# blog/models.py
from django.db import models

class Activite(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
