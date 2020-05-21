from django.db import models

# Create your models here.
class Item(models.Model):
	title = models.CharField(max_length=50)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.title