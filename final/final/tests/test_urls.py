from django.test import SimpleTestCase
from django.urls import reverse, resolve
from invest.views import IndexView, CompanyView, CompanyListView, AddCompanyView, IndicatorView, \
    IndicatorListView, AddIndicatorView, NyseCompaniesView, GpwCompaniesView, MyLoginFinal, MyLogoutView, \
    RSIView, StrategyListView, StrategyView, AddEmailView



class TestUrls(SimpleTestCase):

    def test_IndexView_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_CompanyView_is_resolved(self):
        url = reverse('company', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CompanyView)

    def test_CompanyListView_is_resolved(self):
        url = reverse('companies')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CompanyListView)

    def test_AddCompanyView_is_resolved(self):
        url = reverse('add_company')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddCompanyView)

    def test_IndicatorView_is_resolved(self):
        url = reverse('indicator', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, IndicatorView)

    def test_IndicatorListView_is_resolved(self):
        url = reverse('indicators')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, IndicatorListView)

    def test_AddIndicatorView_is_resolved(self):
        url = reverse('add_indicator')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddIndicatorView)

    def test_NyseCompaniesView_is_resolved(self):
        url = reverse('companies_nyse')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, NyseCompaniesView)

    def test_GpwCompaniesView_is_resolved(self):
        url = reverse('companies_gpw')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, GpwCompaniesView)

    def test_MyLoginFinal_is_resolved(self):
        url = reverse('my_login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, MyLoginFinal)

    def test_MyLogoutView_is_resolved(self):
        url = reverse('my_logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, MyLogoutView)

    def test_RSIView_is_resolved(self):
        url = reverse('rsi', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RSIView)

    def test_StrategyListView_is_resolved(self):
        url = reverse('strategies')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, StrategyListView)

    def test_StrategyView_is_resolved(self):
        url = reverse('strategy', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, StrategyView)

    def test_AddEmailView_is_resolved(self):
        url = reverse('subscription')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddEmailView)
