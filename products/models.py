from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from django import forms
from django.utils import timezone
from django.utils.timezone import now
from django.core.exceptions import ValidationError
# Create your models here.
import json
from django.contrib.auth import get_user_model
User = get_user_model()

file = open('/home/ubuntu/Bureau/news/products/wilayas.json')
data = json.load(file)
WILAYAS_CHOICES = []
for el in data :
    WILAYAS_CHOICES.append((el['name'],el['name']))
def clean_number(number):
    number = str(number)
    if len(number) == 9:
        print(number[:2])
        if number[:1] != '5' and  number[:1] != '7' and number[:1] != '6':
            raise ValidationError('This is not a valid phone number')
    else:
        raise ValidationError('This is not a valid phone number')
    return int(number)

def clean_nompren(n):
        if ' ' not in n:
            raise ValidationError('This is not a valid name and last name')
        return n.lower()
"""class Comm(models.Model):
    commune = models.CharField(max_length=200)
    def __str__(self):
        return self.commune"""

class Product(models.Model):
    nometpren = models.CharField(max_length=120, validators=[clean_nompren])
    telephone = models.DecimalField(max_digits=10, decimal_places=0, validators=[clean_number])
    telephone1 = models.DecimalField(max_digits=10, decimal_places=0, validators=[clean_number],blank = False, null = True)
    wilaya = models.CharField(max_length=200, choices = WILAYAS_CHOICES)
    commune = models.CharField(max_length=200)
    #commune = models.ForeignKey(comm,on_delete=models.SET_DEFAULT, default='unknown category')
    adresse = models.CharField(max_length= 200) 
    montant = models.DecimalField(max_digits=10,decimal_places=0)
    numerocommande = models.DecimalField(max_digits=10,decimal_places=0)
    poids = models.DecimalField(max_digits=4,decimal_places=0)
    remarque = models.CharField(max_length=100,blank = False, null = True) 
    produit = models.CharField(max_length= 200,blank = False, null = True) 
    date = models.DateTimeField(default=timezone.now)

    TYPE_ENVOI_CHOICES = [
        ('V', '---------'),
        ('livraison', 'livraison'),
        ('??change', '??change'),
        ('Pick up', 'Pick up'),
        ('recouvrement', 'recouvrement'),
    ]
    typeenvoi = models.CharField(max_length=100, choices = TYPE_ENVOI_CHOICES, default= "V")

    TYPE_PRESENTATION_CHOICES = [
        ('V', '---------'),
        ('?? domicile', '?? domicile'),
        ('Stop desk', 'Stop desk'),
    ]
    typeprestation = models.CharField(max_length=100, choices = TYPE_PRESENTATION_CHOICES, default= "V")

    pretaexpedier = models.BooleanField(default=True)
    enramassage = models.BooleanField(default=False)
    entransit = models.BooleanField(default=False)
    enhub = models.BooleanField(default=False)
    enlivraison = models.BooleanField(default=False)
    suspendus = models.BooleanField(default=False)
    pay??s = models.DecimalField(max_digits=10,decimal_places=0,default=0,blank = False, null = True)
    retour_chez_livreur = models.BooleanField(default=False)

    email = models.EmailField(max_length = 100, default='soraya@gmail.com')
    checked = models.BooleanField(default = False)


    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})

class Feedback(models.Model):
    id_user = models.DecimalField(max_digits=10000, decimal_places=0,blank = False, null = True)
    comment = models.TextField()