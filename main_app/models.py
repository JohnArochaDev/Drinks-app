from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class ShoppingGuide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    drink_id = models.CharField(max_length=20)
    drink_image = models.CharField(max_length=255)
    ingredient_1 = models.CharField(max_length=255, blank=True)
    ingredient_2 = models.CharField(max_length=255, blank=True)
    ingredient_3 = models.CharField(max_length=255, blank=True)
    ingredient_4 = models.CharField(max_length=255, blank=True)
    ingredient_5 = models.CharField(max_length=255, blank=True)
    ingredient_6 = models.CharField(max_length=255, blank=True)
    ingredient_7 = models.CharField(max_length=255, blank=True)
    ingredient_8 = models.CharField(max_length=255, blank=True)
    ingredient_9 = models.CharField(max_length=255, blank=True)
    ingredient_10= models.CharField(max_length=255, blank=True)
    ingredient_11= models.CharField(max_length=255, blank=True)
    ingredient_12= models.CharField(max_length=255, blank=True)
    ingredient_13= models.CharField(max_length=255, blank=True)
    ingredient_14= models.CharField(max_length=255, blank=True)
    ingredient_15= models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'list_id': self.id})