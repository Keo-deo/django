from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def arvore_view(request):
    return render(request, "arvore/home.html")