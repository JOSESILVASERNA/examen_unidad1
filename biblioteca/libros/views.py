from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Libro
from .forms import libroAddForms

# Create your views here.
def home123(request):
    m = "Hola biblioteca"
    contexto = {"mensaje":m}
    return render(request, 'home.html', contexto)


def lista_libros(request):
    libr = Libro.objects.all()
    print request
    i= "Libros"
    template = "listaDeLibros.html"
    context  = {"mensaje": i, "libro": libr}
    return render(request, template, context)


def detalle(request, object_id=None):
    #Logico de negocio alias hechizo
    l = get_object_or_404(Libro, id=object_id)
    mensaje = "Libros nuevo!!!!!@!!!!1!"
    template = "detalleLibro.html"
    contexto= {"mensaje":mensaje,
               "libro": l }
    return render(request, template, contexto)


def detalle_slug(request, slug=None):
    #Logico de negocio alias hechizo
    print "hola"
    try:
        l  = get_object_or_404(Libro, slug=slug)
    except Libro.MultipleObjectsReturned:
        l = Libro.objects.filter(slug=slug).order_by("-name").first()
    print l
    m = "libros nuevo"
    template = "detalleLibro.html"
    contexto= {"mensaje":m,
           "libro": l }
    return render(request, template, contexto)

def agregar_libro(request, object_id=None):
    form = libroAddForms(request.POST or None)
    if request.method == "POST":
        print request.POST
    if form.is_valid():
        # print request.POST
        data = form.cleaned_data
        name = data.get("name")
        autor = data.get("autor")
        editorial = data.get("editorial")
        ISBN = data.get("ISBN")
        precio = data.get("precio")
        # nuevo_producto = Producto.object.create(nombre = nombre,
        #                                         descripcion = descripcion,
        #                                         precio = precio)
        nuevo_libro = Libro()
        nuevo_libro.name = name
        nuevo_libro.autor = autor
        nuevo_libro.editorial = editorial
        nuevo_libro.ISBN = ISBN
        nuevo_libro.precio = precio
        nuevo_libro.save()

    template = "agregar_libro.html"
    context = {
        "form":form
    }

    return render(request, template, context)
