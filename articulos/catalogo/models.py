from django.db import models


# Create your models here.
from django.db import models
from django.urls import reverse
import uuid
class Producto(models.Model):
    id=models.IntegerField(primary_key=True, help_text="Código del producto")
    nom=models.CharField(max_length=200)
    cant=models.IntegerField()
    def __str__(self):
        return self.nom