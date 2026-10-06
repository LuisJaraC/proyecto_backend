from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#  Router API
router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet, basename='ticket')
router.register(r'historial', views.HistorialTicketViewSet, basename='historial')

urlpatterns = [
    # Ruta API
    path('api/', include(router.urls)),
    
    # Ruta HTML 
    path('', views.bienvenida_view, name='bienvenida'),
]