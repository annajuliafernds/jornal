from django.urls import path, include
from .views import IndexView, CadastroView, LoginView, NoticiaDetailView, logout_view, ComentarView, ListarEdicoesView, ListarNoticiaPorEdicaoView, CadastrarNoticiaView

app_name = 'jornal'  # Usado para identificar as URLs pelos nomes em vez de toda a URL, ex: 'jornal:index'

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),  # Mapeamento para a view Index
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('noticia/<int:pk>/', NoticiaDetailView.as_view(), name='noticia_detalhe'),
    path('logout/', logout_view, name='logout'),  # Corrigido para usar a função de logout
    path('comentar/<int:pk>/', ComentarView, name='comentar'),
    path('edicoes/', ListarEdicoesView.as_view(), name='listar_edicoes'),
    path('noticias/<int:pk>/', ListarNoticiaPorEdicaoView.as_view(), name='listar_noticias'),
    path('nova-noticia/', CadastrarNoticiaView.as_view(), name='nova-noticia'),
]
