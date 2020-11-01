from django.shortcuts import render
from . models import Producto
from django.views import generic

# Create your views here.
def Index(request) :
    produ = Producto.objects.all().count()

    return render(
        request,
        'index.html',
        context={'produ': produ},
    )