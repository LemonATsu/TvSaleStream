from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 20)
	price = models.DecimalField(max_digits=10,decimal_places=0)
	owner = models.DecimalField(max_digits=10,decimal_places=0)
	live = models.DecimalField(max_digits=2,decimal_places=0,default=0)
	ownerName = models.CharField(max_length = 20)
