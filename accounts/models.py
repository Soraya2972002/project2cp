from django.db import models
from django.contrib.auth.models import AbstractUser
import json
from django.core.exceptions import ValidationError

file = open('/home/ubuntu/Bureau/news/products/wilayas.json')
data = json.load(file)
WILAYAS_CHOICES = []
for el in data :
    WILAYAS_CHOICES.append((el['name'],el['name']))
WILAYAS_CHOICES.append(("",''))

def clean_number(number):
    number = str(number)
    if len(number) == 10:
        print('here')
        print(number[:2])
        if number[:2] != '05' and  number[:2] != '07' and number[:2] != '06':
            raise ValidationError('This is not a valid phone number')
    return number

class CustomUser(AbstractUser):
    wilaya = models.CharField(max_length=100, choices = WILAYAS_CHOICES, default='')
    num = models.DecimalField(max_digits=10,decimal_places=0, unique=True, default= 0000000000, validators = [clean_number])
    email = models.EmailField(unique=True)
    #these are the fields for livreur
    disponible = models.BooleanField(default = True)
    en_cours_livraison = models.CharField(max_length = 8000,default = '')
    livres = models.CharField(max_length = 800000000,default = '')
    date = models.DateTimeField(blank = False, null = True)