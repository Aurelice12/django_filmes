from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),

    path('diretores/', views.listar_diretores, name='listar_diretores'),
    path('diretores/criar/', views.criar_diretor, name='criar_diretor'),
    path('diretores/editar/<int:id>/', views.editar_diretor, name='editar_diretor'),
    path('diretores/deletar/<int:id>/', views.deletar_diretor, name='deletar_diretor'),

    path('filmes/', views.listar_filmes, name='listar_filmes'),
    path('filmes/criar/', views.criar_filme, name='criar_filme'),
    path('filmes/editar/<int:id>/', views.editar_filme, name='editar_filme'),
    path('filmes/deletar/<int:id>/', views.deletar_filme, name='deletar_filme'),
]
