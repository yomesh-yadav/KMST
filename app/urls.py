from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name=''),
   path('get_relations', views.get_relations, name=''),
]