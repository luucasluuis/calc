from django.urls import path
from . import views

app_name = 'calc'

urlpatterns = [
    path('exemplo/', views.exemplo, name='exemplo'),
    path('', views.calculando, name='atualizar_numero'),

]
