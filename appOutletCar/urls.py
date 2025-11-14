from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ofertas/', views.index_ofertas, name='lista_ofertas'),
    path('ofertas/<int:idCoche>/', views.ver_oferta, name='ver_oferta'),
    path('marcas/', views.visualizar_marcas, name='visualizar_marcas'),
    path('marcas/<int:idMarca>', views.ver_marca, name='verMarca'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:idCat>/', views.detalle_categoria, name='detalle_categoria'),

]