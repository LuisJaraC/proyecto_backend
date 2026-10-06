from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model): 
    ESTADOS = [
        ('abierto', 'Abierto'),
        ('en_proceso', 'En Proceso'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='abierto')
    
    # Relaciones con usuarios (Cliente que lo crea y Técnico asignado)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_creados')
    tecnico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_asignados')
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.get_estado_display()}"

class HistorialTicket(models.Model): # <-- Aquí también
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='historial')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    comentario = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historial de {self.ticket.titulo} el {self.fecha_registro}"