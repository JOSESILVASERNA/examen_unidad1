from __future__ import unicode_literals
from django.db.models.signals import pre_save
from django.utils.text import slugify
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
def libro_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = slugify(instance.nombre)

pre_save.connect(libro_pre_save_reciever, sender=Libro)
