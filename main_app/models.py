from django.db import models

# Create your models here.
class Catch(models.Model):
    species = models.CharField(max_length=100)
    length = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return self.species