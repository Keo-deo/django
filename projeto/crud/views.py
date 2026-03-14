from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
# Create your views here.

cliente = MongoClient("mongodb://localhost:27017")

db = cliente["django"]

colection = db["dejango"]

def crud_view(request):
    return render(request, "crud/main.html")

def get_adicionar_view(request):
    return render(request, "crud/get_adicionar.html")

def pull_adicionar_view(request):
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

        return render(request, "crud/pull_adicionar.html", contexto)
    
    return HttpResponse("Método não permitido", status=405)


def pull_exibir_view(request):
    jogadores = list(colection.find())
    contexto = {
        "jogadores": jogadores
    }
        

    return render(request, "crud/pull_exibir.html", contexto)


def get_deletar_view(request):
    return render(request, "crud/get_deletar.html")

def pull_deletar_view(request):
    if request.method == 'POST':
        # 'nome_usuario' é o valor do atributo 'name' no HTML
        nome = request.POST.get('nome_usuario')

        item = colection.find_one({"nome": nome})
        colection.delete_one(item)

        contexto = {
            "nome": nome
        }

        return render(request, "crud/pull_deletar.html", contexto)
    
    return HttpResponse("Método não permitido", status=405)
