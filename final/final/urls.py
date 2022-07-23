"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from invest.views import IndexView, CompanyView, CompanyListView, AddCompanyView, IndicatorView, \
    IndicatorListView, AddIndicatorView, NyseCompaniesView, GpwCompaniesView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    #path('RSI/', RSIView.as_view()),
    path('company/<int:company_id>/', CompanyView.as_view()),
    path('companies/', CompanyListView.as_view()),
    path('add_company/', AddCompanyView.as_view()),
    path('indicator/<int:indicator_id>/', IndicatorView.as_view()),
    path('indicators/', IndicatorListView.as_view()),
    path('add_indicator/', AddIndicatorView.as_view()),
    path('companies/nyse/', NyseCompaniesView.as_view()),
    path('companies/gpw/', GpwCompaniesView.as_view()),
]
