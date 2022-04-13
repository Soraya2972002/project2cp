from django.db import models
from django.urls import reverse
from django import forms
# Create your models here.
import json

file = open('/home/ubuntu/Bureau/news/products/wilayas.json')
data = json.load(file)
WILAYAS_CHOICES = []
for el in data :
    WILAYAS_CHOICES.append(("Wilaya",el['name']))

class Product(models.Model):
    nometpren = models.CharField(max_length=120)
    telephone = models.DecimalField(max_digits=10, decimal_places=0, unique=True)
    telephone1 = models.DecimalField(max_digits=10, decimal_places=0, unique= True)
    wilaya = models.CharField(max_length=10, choices = WILAYAS_CHOICES)
    commune = models.CharField(max_length=10)
    adresse = models.CharField(max_length= 200) 
    montant = models.DecimalField(max_digits=10,decimal_places=5)
    numerocommande = models.DecimalField(max_digits=10,decimal_places=0)
    poids = models.DecimalField(max_digits=4,decimal_places=0)
    remarque = models.TextField(max_length=100) 
    produit = models.TextField(blank = False, null = True) 

    TYPE_ENVOI_CHOICES = [
        ('V', 'livraison'),
        ('EC', 'échange'),
        ('PU', 'Pick up'),
        ('RE', 'recouvrement'),
        ('V', '---------'),
    ]
    typeenvoi = models.CharField(max_length=100, choices = TYPE_ENVOI_CHOICES, default= "V")

    TYPE_PRESENTATION_CHOICES = [
        ('V', '---------'),
        ('AD', 'à domicile'),
        ('SD', 'Stop desk'),
    ]
    typeprestation = models.CharField(max_length=100, choices = TYPE_PRESENTATION_CHOICES, default= "V")

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
    