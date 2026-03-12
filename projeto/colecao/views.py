from django.shortcuts import render


def colecao_view(request):
    return render(request, "colecao/colecao.html")