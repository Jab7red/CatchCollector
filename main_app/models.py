from django.db import models

from django.urls import reverse

# Create your models here.
class Catch(models.Model):
    species = models.CharField(max_length=100)
    length = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse('detail', kwargs={'catch_id': self.id})