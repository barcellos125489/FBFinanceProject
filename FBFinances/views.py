from django.shortcuts import render

def index(request):
    """Página principal"""
    return render(request, 'FBFinances/index.html')

# Create your views here.
