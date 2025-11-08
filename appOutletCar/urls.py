from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('ofertas/', views.index_ofertas, name='lista_ofertas'),
 path('ofertas/<int:idOferta>/', views.ver_oferta, name='ver_oferta')
]