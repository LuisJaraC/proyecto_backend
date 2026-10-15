from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Ticket, HistorialTicket
from .serializers import TicketSerializer, HistorialTicketSerializer

# Vista Pública 
def bienvenida_view(request):
    return render(request, 'index.html')

# Vista Protegida 
@login_required
def vista_protegida_por_funcion(request):
    tickets_count = Ticket.objects.count()
    return render(request, 'protegida_por_funcion.html', {'tickets_count': tickets_count})

# Vista Protegida Basada en Clases 
class VistaProtegidaPorClase(LoginRequiredMixin, TemplateView):
    template_name = 'protegida_por_clase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historial_count'] = HistorialTicket.objects.count()
        return context

# Vista de Error 404
def error_400_view(request, exception):
    return render(request, 'error_400.html')

# ViewSets de la API RESTful
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class HistorialTicketViewSet(viewsets.ModelViewSet):
    queryset = HistorialTicket.objects.all()
    serializer_class = HistorialTicketSerializer