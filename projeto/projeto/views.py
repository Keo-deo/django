from django.shortcuts import render

def home_view(request):
    return render(request, "homepage.html")

def arvore_view(request):
    return render(request, "arvore/home.html")

def colecao_view(request):
    return render(request, "colecao/colecao.html")