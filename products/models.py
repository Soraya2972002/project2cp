from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank = False, null = True) 
    featured = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
    