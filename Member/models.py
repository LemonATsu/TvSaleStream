from django.db import models

# Create your models here.
class Account(models.Model):
    acc = models.CharField(max_length=20)
    pwd = models.CharField(max_length=200)
    online = models.DecimalField(max_digits=2,decimal_places=0)



