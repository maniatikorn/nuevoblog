from django.shortcuts import render
from .models import Articulo
from django.views.generic import ListView, DetailView
# Create your views here.

class IndexView(ListView):
	template_name = 'index.html'
	model = Articulo

class ArticuloDetailView(DetailView):
	template_name = 'detalle.html'
	model = Articulo