from django.urls import path
from . import views


urlpatterns = [
    path('', views.bienvenida_view, name='index')
]