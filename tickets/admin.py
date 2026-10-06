from django.contrib import admin
from .models import Ticket, HistorialTicket


admin.site.register(Ticket)
admin.site.register(HistorialTicket)