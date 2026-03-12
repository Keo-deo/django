from django.urls import path, include
from . import views

app_name = "parentes"

urlpatterns = [
    path("", views.parentes_view, name="home"),
    path("alyne/", views.alyne_view, name="alyne"),
    path("eudes/", views.eudes_view, name="eudes"),
    path("hebel/", views.hebel_view, name="hebel"),
    path("nyra/", views.nyra_view, name="nyra"),
    path("magali/", views.magali_view, name="magali"),
    path("marucia/", views.marucia_view, name="marucia"),
    path("lenira/", views.lenira_view, name="lenira"),
    path("irmaos/", views.irmaos_view, name="irmaos"),
    path("irmaos/miguel", views.miguel_view, name="miguel"),
    path("irmaos/mirela", views.mirela_view, name="mirela"),
    path("irmaos/miryan", views.miryan_view, name="miryan"),
    path("irmaos/yan", views.yan_view, name="yan"),
    path("tios/", views.tios_view, name="tios"),
    path("tios/vitor", views.vitor_view, name="vitor"),
    path("tios/jader", views.jader_view, name="jader"),
    path("primos/", views.primos_view, name="primos"),
    path("primos/valentina", views.valentina_view, name="valentina"),
    path("primos/benjamim", views.benjamim_view, name="benjamim"),
]