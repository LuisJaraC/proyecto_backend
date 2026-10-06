from rest_framework import serializers
from .models import Ticket, HistorialTicket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class HistorialTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialTicket
        fields = '__all__'