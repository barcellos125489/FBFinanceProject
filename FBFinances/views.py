from django.shortcuts import render

def index(request):
    """Página principal"""
    return render(request, 'FBFinances/index.html')

def loans(request):
    """Página que contém todos os tipos de empréstimos e seus resultados"""
    return render(request, 'FBFinances/loans.html')

def IR(request):
    """Página que contém o cálculo do imposto de renda de acordo com seu salário"""
    return render(request, 'FBFinances/IR.html')

def stocks(request, ticker):
    """Página que contém uma ação e análises feitas com data science e notícias conseguidas por web scrapping sobre essa ação"""
    return render(request, 'FBFinances/stocks.html')

# Create your views here.
