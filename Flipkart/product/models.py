from django.db import models

# Create your models here.

class Product(models.Model): 
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()  
    quantity = models.IntegerField()  

    def __str__(self):
        return self.name
