from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views

# Router API REST
router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet, basename='ticket')
router.register(r'historial', views.HistorialTicketViewSet, basename='historial')

urlpatterns = [
    # Rutas API RESTful
    path('api/', include(router.urls)),
    
    # Ruta Pública de Bienvenida
    path('', views.bienvenida_view, name='bienvenida'),

    # Rutas de Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Rutas Protegidas
    path('dashboard-por-funcion/', views.vista_protegida_por_funcion, name='protegida_por_funcion'),
    path('panel-por-clase/', views.VistaProtegidaPorClase.as_view(), name='protegida_por_clase'),
]