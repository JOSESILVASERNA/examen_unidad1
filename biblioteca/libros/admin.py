from django.contrib import admin
from libros.models import Libro
# Register your models here.



class books(admin.ModelAdmin):
    list_display= ["ISBN","name","autor","editorial","precio"]
    search_field= ['name',"autor","editorial"]
    list_editable= ["precio", "name"]
    list_filter= ["precio", "name"]

    class Meta:
        model = Libro

admin.site.register(Libro, books)
