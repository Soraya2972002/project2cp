from django.db import models
from django.contrib.auth.models import AbstractUser
import json

file = open('/home/ubuntu/Bureau/news/products/wilayas.json')
data = json.load(file)
WILAYAS_CHOICES = []
for el in data :
    WILAYAS_CHOICES.append((el['name'],el['name']))
WILAYAS_CHOICES.append(("Livreur",''))

class CustomUser(AbstractUser):
    wilaya = models.CharField(max_length=100, choices = WILAYAS_CHOICES, default='Livreur')