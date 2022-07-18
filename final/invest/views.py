from django.shortcuts import render
from django.views import View
import yfinance as yf, pandas as pd, shutil, os, time, glob
import numpy as np
import requests
from get_all_tickers import get_tickers as gt
from statistics import mean
# Create your views here.

class IndexView(View):

    def get(self, request):
        return render(request, "index.html",)

import pandas_datareader as pdr
from datetime import datetime
#from datetime import date

#today = date.today()
ticker = pdr.get_data_yahoo("TWTR", datetime(2022, 1, 1))
delta = ticker['Close'].diff()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down
ticker['RSI'] = 100 - (100/(1 + rs))
# Skip first 14 days to have real values
ticker = ticker.iloc[14:]
print(ticker)
