from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Company, Stock, Indicator, Strategy, Subscription
from .forms import AddCompanyForm, AddIndicatorForm, MyLoginForm, SubscriptionForm, CreateUserForm
from django.contrib.auth import authenticate, logout
from django.contrib import messages
import pandas_datareader as pdr
from datetime import datetime

# Create your views here.


class IndexView(View):
    def get(self, request):
        form = SubscriptionForm()
        company = get_object_or_404(Company, pk=1)
        company1 = get_object_or_404(Company, pk=2)
        company2 = get_object_or_404(Company, pk=3)
        company3 = get_object_or_404(Company, pk=4)
        company4 = get_object_or_404(Company, pk=5)
        company5 = get_object_or_404(Company, pk=6)
        return render(request, "index.html", {"form": form,
                                              "company": company,
                                              "company1": company1,
                                              "company2": company2,
                                              "company3": company3,
                                              "company4": company4,
                                              "company5": company5,
                                              })

    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            Subscription.objects.create(email=email)
            return redirect(f'/subscription/')
        else:
            return HttpResponse('Formularz jest niepoprawny!', {"form": form})


class CompanyView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        stock = company.stock
        return render(request, 'company.html', {'company': company, 'stock': stock})


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
            stock = form.cleaned_data["stock"]
            description = form.cleaned_data["description"]
            history = form.cleaned_data["history"]
            new_company = Company.objects.create(name=name, short_name=short_name,
                                                 stock=Stock.objects.get(stock_name=stock),
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
        companies = Company.objects.filter(stock=stock)
        return render(request, 'nyse_companies.html', {'companies': companies})


class GpwCompaniesView(View):
    def get(self, request):
        stock = Stock.objects.get(pk=2)
        companies = Company.objects.filter(stock=stock)
        return render(request, 'gpw_companies.html', {'companies': companies})


class MyLoginFinal(View):

    def get(self, request):
        form = MyLoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = MyLoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=login, password=password)
            if user is not None:
                return render(request, 'login_succes.html', {"form": form})
            else:
                return HttpResponse("Zły użytkownik lub hasło")


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('my_login'))


class RSIView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        ticker = pdr.get_data_yahoo(company.short_name, datetime(2022, 1, 1))
        delta = ticker['Close'].diff()
        up = delta.clip(lower=0)
        down = -1 * delta.clip(upper=0)
        ema_up = up.ewm(com=13, adjust=False).mean()
        ema_down = down.ewm(com=13, adjust=False).mean()
        rs = ema_up / ema_down
        ticker['RSI'] = 100 - (100 / (1 + rs))
        ticker = ticker.iloc[14:]
        ticker = ticker.iloc[-1:]
        result = str(ticker['RSI'])
        result1 = []
        for i in result:
            result1 += i.split(" ")
            result2 = "".join(result1[23:31])
        return render(request, "RSI.html", context={
                       'RSIView': RSIView,
                       'ticker': ticker,
                        'result': result,
                        'company': company,
                        'result2': result2,
                  })


class StrategyView(View):
    def get(self, request, strategy_id):
        strategy = get_object_or_404(Strategy, pk=strategy_id)
        return render(request, 'strategy.html', {'strategy': strategy})


class StrategyListView(View):
    def get(self, request):
        strategies = Strategy.objects.all().order_by('name')
        return render(request, 'strategy_list.html', {'strategies': strategies})


class AddEmailView(View):
    def get(self, request):
        return render(request, 'subscription.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('my_login')

    context = {'form': form}
    return render(request, 'register.html', context)
