from django.db import models

# Create your models here.

class MessageBox(models.Model):
	user = models.CharField(max_length=50)
	message = models.CharField(max_length=200)
