from django.urls import path, include
from . import views

app_name = "parentes"

urlpatterns = [
    path("", views.parentes_view, name="home"),
    path("hebel/", views.hebel_view)
]