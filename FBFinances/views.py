from django.shortcuts import render

def index(request):
    """Landing page"""
    return render(request, 'FBFinances/index.html')

def loans(request):
    """Page that contains all loans, finance and their calculations"""
    return render(request, 'FBFinances/loans.html')

def IR(request):
    """Page that contains income tax calculations"""
    return render(request, 'FBFinances/IR.html')

def stocks(request, ticker):
    """Page that contains a stock and its analysis made with data science along with news about it reached with web scrapping"""
    return render(request, 'FBFinances/stocks.html')

def cripto(request, coin):
    """Page that contains a cripto coin and its analysis made with data science along with news about it reached with web scrapping"""
    return render(request, 'FBFinances/coins.html')

def tracksheet(request, username):
    """Page that contains informations about the user's moneyflow"""
    return render(request, 'FBFinances/tracksheet.html')

# Create your views here.
