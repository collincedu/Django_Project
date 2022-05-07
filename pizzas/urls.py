from django.urls import path

from . import views
import pizzas

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
]