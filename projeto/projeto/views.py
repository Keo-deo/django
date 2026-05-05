from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017")

db = cliente["django"]

colection = db["dejango"]

def home_view(request):
    return render(request, "homepage.html")

def arvore_view(request):
    return render(request, "arvore/home.html")

def colecao_view(request):
    return render(request, "colecao/colecao.html")

def adicionar_view(request):
    if request.method == 'POST':
        # 'nome_usuario' é o valor do atributo 'name' no HTML
        nome = request.POST.get('nome_usuario')

        informacoes = {
            "nome": nome
        }

        colection.insert_one(informacoes)

        contexto = {
            "nome": nome
        }

        return render(request, "crud/adicionar.html", contexto)
    
    return HttpResponse("Método não permitido", status=405)

def mgay_view(request):
    return render(request, "parentes/mgay.html")

