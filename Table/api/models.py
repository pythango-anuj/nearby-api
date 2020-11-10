from django.db import models

# Create your models here.
class Nearby(models.Model):
	type = models.CharField(max_length=100)
	address = models.CharField(max_length=250)
	charger_id = models.CharField(max_length=100)

	def __str__(self):
		return self.type
	
