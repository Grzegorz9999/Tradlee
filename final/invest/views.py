from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Company, Stock
import yfinance as yf, pandas as pd, shutil, os, time, glob
import numpy as np
import requests
from get_all_tickers import get_tickers as gt
from statistics import mean
import pandas_datareader as pdr
from datetime import datetime

# Create your views here.

class IndexView(View):

    def get(self, request):
        return render(request, "index.html", )




# from datetime import date

# today = date.today()
ticker = pdr.get_data_yahoo("TWTR", datetime(2022, 5, 1))
delta = ticker['Close'].diff()
up = delta.clip(lower=0)
down = -1 * delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up / ema_down
ticker['RSI'] = 100 - (100 / (1 + rs))
# Skip first 14 days to have real values
ticker = ticker.iloc[14:]
ticker1 = ticker.iloc[-1:]
print(ticker)
print(ticker1)

def get_rsi(self, request):
    ticker = pdr.get_data_yahoo("TSLA", datetime(2022, 1, 1))
    delta = ticker['Close'].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ema_up = up.ewm(com=13, adjust=False).mean()
    ema_down = down.ewm(com=13, adjust=False).mean()
    rs = ema_up / ema_down
    ticker['RSI'] = 100 - (100 / (1 + rs))
    # Skip first 14 days to have real values
    # ticker = ticker.iloc[14:]
    ticker = ticker.iloc[-1:]
    print(ticker['RSI'])
    return render(request, "RSI.html", context={
        'ticker': ticker,
    })

class CompanyView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        stock_names = company.stock_names.all()
        return render(request, 'company.html', {'company': company, 'stock_names': stock_names})

class CompanyListView(View):
    def get(self, request):
        companies = Company.objects.all().order_by('name')
        return render(request, 'company_list.html', {'companies': companies})

#class RSIView(View):
#    def get(self, request):
  #      ticker = pdr.get_data_yahoo("TSLA", datetime(2022, 1, 1))
   #     delta = ticker['Close'].diff()
  #      up = delta.clip(lower=0)
  #      down = -1 * delta.clip(upper=0)
  #      ema_up = up.ewm(com=13, adjust=False).mean()
  #      ema_down = down.ewm(com=13, adjust=False).mean()
  #      rs = ema_up / ema_down
  #      ticker['RSI'] = 100 - (100 / (1 + rs))
  ## #     # ticker = ticker.iloc[14:]
   #     ticker = ticker.iloc[-1:]
   #     print(ticker['RSI'])
  #      return render(request, "RSI.html", context={
   #                   'RSIView': RSIView,
   #                     'ticker': ticker,
    #              })
