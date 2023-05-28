from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('new',views.new_persona, name='new_personas'),
    path('delete/<int:id>/',views.delete_persona, name='delete_personas'),
    path('update/<int:id>/',views.update_persona, name='update_personas'),
    path('ciudad/new',views.new_ciudad, name='new_ciudades'),
    path('ciudad/delete/<int:id>/',views.delete_ciudad, name='delete_ciudades'),
    path('ciudad/update/<int:id>/',views.update_ciudad, name='update_ciudades'),
    path('tipodoc/new',views.new_tipodoc, name='new_tipodocs'),
    path('tipodoc/delete/<int:id>/',views.delete_tipodoc, name='delete_tipodocs'),
    path('tipodoc/update/<int:id>/',views.update_tipodoc, name='update_tipodocs'),
]