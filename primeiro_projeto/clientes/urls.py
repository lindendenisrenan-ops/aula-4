from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('hello/', views.hello , name="hello"),
    path('bye/', views.bye , name="bye"),
    path('excluir/', views.excluir , name="excluir"),
    path('clientes/', views.clientes , name="clientes"),
    path('sobre/', views.sobre , name="sobre"),
]