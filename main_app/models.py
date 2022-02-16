
from django.db import models

from django.urls import reverse

# A tuple of 2-tuples
COLORS = (
    ('R', 'Red'),
    ('W', 'White'),
    ('B', 'Blue'),
    ('G', 'Green'),
    ('Y', 'Yellow'),
    ('S', 'Shad')
)

# Create your models here.
class Catch(models.Model):
    species = models.CharField(max_length=100)
    length = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse('detail', kwargs={'catch_id': self.id})




class Gear(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(
        max_length=100, 
        choices=COLORS, 
        default=COLORS[0][0]
    )
    # Create a catch_id FK
    catch = models.ForeignKey(Catch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_color_display()} on {self.name}"