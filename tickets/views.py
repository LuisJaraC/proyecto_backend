from django.shortcuts import render
from rest_framework import viewsets
from .models import Ticket, HistorialTicket
from .serializers import TicketSerializer, HistorialTicketSerializer

# Create your views here.
def bienvenida_view (request):
    return render(request, 'index.html')

def error_400_view (request, exception):
    return render(request, 'error_400.html')

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class HistorialTicketViewSet(viewsets.ModelViewSet):
    queryset = HistorialTicket.objects.all()
    serializer_class = HistorialTicketSerializer