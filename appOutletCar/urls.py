from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('ofertas/', views.index_ofertas, name='lista_ofertas'),
    path('ofertas/<int:idOferta>/', views.ver_oferta, name='ver_oferta'),
    path('marcas/', views.visualizar_marcas, name='visualizar_marcas'),
    path('marcas/<int:idMarca>', views.ver_marca, name='verMarca'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:idCat>/', views.detalle_categoria, name='detalle_categoria'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
