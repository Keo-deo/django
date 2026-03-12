from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.colecao_view),
]