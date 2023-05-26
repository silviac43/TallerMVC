from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('new',views.new_persona, name='new_personas'),
]