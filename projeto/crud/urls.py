from django.urls import path, include
from . import views

app_name = "crud"

urlpatterns = [
    path("", views.crud_view, name="main"),
    path("get_adicionar/", views.get_adicionar_view, name="get_adicionar"),
    path("pull_adicionar/", views.pull_adicionar_view, name="pull_adicionar"),

    path("pull_exibir/", views.pull_exibir_view, name="pull_exibir"),

    path("get_deletar/", views.get_deletar_view, name="get_deletar"),
    path("pull_deletar/", views.pull_deletar_view, name="pull_deletar"),
]