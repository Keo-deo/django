from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.arvore_view),
    path("parentes/", include("parentes.urls"))
]