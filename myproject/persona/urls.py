from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('new',views.new_persona, name='new_personas'),
    path('delete/<int:id>/',views.delete_persona, name='delete_personas'),
]