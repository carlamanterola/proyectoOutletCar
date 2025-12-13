from django.urls import path
from . import views, views_forms
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.index, name='index'),
    path('ofertas/', views.index_ofertas, name='lista_ofertas'),
    path('ofertas/<int:idOferta>/', views.ver_oferta, name='ver_oferta'),
    path('marcas/', views.visualizar_marcas, name='visualizar_marcas'),
    path('marcas/<int:idMarca>', views.ver_marca, name='verMarca'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:idCat>/', views.detalle_categoria, name='detalle_categoria'),
    path('ofertas/formulario/', views_forms.procesar_form_coche , name='procesar_form'),
    path('combustible/<int:idCombustible>/', views.combustible, name='detalle_combustible'),
    path('coche/eliminar/<int:pk>/', views.eliminar_coche, name='eliminar_coche'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    
    path("favoritos/agregar/<int:coche_id>/", views.agregar_favorito, name="agregar_favorito"),
    path("favoritos/", views.lista_favoritos, name="lista_favoritos"),
    path('coches-mas-baratos/', views.coches_mas_baratos_json, name='coches_mas_baratos_json'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

