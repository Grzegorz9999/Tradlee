from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import Company, Stock, Indicator
from .forms import AddCompanyForm, AddIndicatorForm
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

class AddCompanyView(View):
    def get(self, request):
        form = AddCompanyForm()
        return render(request, "add_company.html", {"form": form})

    def post(self, request):
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            short_name = form.cleaned_data["short_name"]
            description = form.cleaned_data["description"]
            history = form.cleaned_data["history"]
            new_company = Company.objects.create(name=name, short_name=short_name,
                                                 description=description, history=history)
            return redirect(f'/company/{new_company.id}/')
        else:
            return HttpResponse('Formularz jest niepoprawny!', {"form": form})

class IndicatorView(View):
    def get(self, request, indicator_id):
        indicator = get_object_or_404(Indicator, pk=indicator_id)
        return render(request, 'indicator.html', {'indicator': indicator})

class IndicatorListView(View):
    def get(self, request):
        indicators = Indicator.objects.all().order_by('name')
        return render(request, 'indicator_list.html', {'indicators': indicators})

class AddIndicatorView(View):
    def get(self, request):
        form = AddIndicatorForm()
        return render(request, "add_indicator.html", {"form": form})

    def post(self, request):
        form = AddIndicatorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            short_name = form.cleaned_data["short_name"]
            definition = form.cleaned_data["definition"]
            new_indicator = Indicator.objects.create(name=name, short_name=short_name,
                                                 definition=definition)
            return redirect(f'/indicator/{new_indicator.id}/')
        else:
            return HttpResponse('Formularz jest niepoprawny!', {"form": form})

class NyseCompaniesView(View):
    def get(self, request):
        stock = Stock.objects.get(pk=1)
        companies = Company.objects.filter(stock_names=stock)
        return render(request, 'nyse_companies.html', {'companies': companies})

class GpwCompaniesView(View):
    def get(self, request):
        stock = Stock.objects.get(pk=2)
        companies = Company.objects.filter(stock_names=stock)
        return render(request, 'gpw_companies.html', {'companies': companies})

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
