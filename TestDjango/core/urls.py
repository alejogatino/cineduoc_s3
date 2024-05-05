from django.urls import path
#from .views import home, posts

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('', views.home,name="home"),
    path('posts/', views.posts, name='posts'),
    path('detalle/', views.detalle, name='detalle'),
    path('formulario/', views.formulario, name='formulario'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar-sesion'),
    path('form-api-back',views.form_api_back,name="form_api_back"),
    path('api-movie',views.api_movie,name="api_movie"),
    
   

]