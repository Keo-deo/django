from django.shortcuts import render

# Create your views here.
def parentes_view(request):
    return render(request, "parentes/parentes.html")

def hebel_view(request):
    return None
