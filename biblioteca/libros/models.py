from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Libro(models.Model):
    name = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    ISBN = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits = 9999, decimal_places = 2)

    def __unicode__(self):
        return self.name
