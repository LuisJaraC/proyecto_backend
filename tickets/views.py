from django.shortcuts import render

# Create your views here.
def bienvenida_view (request):
    return render(request, 'index.html')

def error_400_view (request, exception):
    return render(request, 'error_400.html')