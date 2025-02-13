from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from users.models import loan , income, finance, expense
import yfinance as yf


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
    ticker_info = yf.Ticker(ticker)
    context = {'ticker_info': ticker_info}

    return render(request, 'FBFinances/stocks.html',context)

def coins(request, coin_name):
    """Page that contains a cripto coin and its analysis made with data science along with news about it reached with web scrapping"""
    return render(request, 'FBFinances/coins.html')

@login_required
def tracksheet(request, userid):
    """Page that contains informations about the user's moneyflow"""
    if userid != request.user.id:
        print(userid)
        print(request.user.id)
        raise Http404
    
    try:
        loans = request.user.loan_set.order_by('date_added')
    except: 
        print('Não existem empréstimos disponíveis para serem mostrados')
        loans = []
    try:
        incomes = request.user.income_set.order_by('date_added')
    except: 
        print('Não existem rendas disponíveis para serem mostrados')
        incomes = []
    try:
        finances = request.user.finance_set.order_by('date_added')
    except: 
        print('Não existem financiamentos disponíveis para serem mostrados')
        finances = []
    try:
        expenses = request.user.expense_set.order_by('date_added')
    except: 
        print('Não existem gastos disponíveis para serem mostrados')
        expenses = []
    
    

    context = {'loans':loans,'incomes':incomes,'finances':finances, 'expenses':expenses}
    return render(request, 'FBFinances/tracksheet.html',context)

# Create your views here.
