from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('persona/', views.lista_persona,name="lista_persona"),
    path('movie/', views.lista_Movie,name="lista_movie"),
    
   

]