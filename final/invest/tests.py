import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
from .models import Stock, Company, Indicator, Strategy, Subscription

# class URLTests(TestCase):
#     def test_testhomepage(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1

@pytest.mark.django_db
def test_view(client):
   url = reverse('index')
   response = client.get(url)
   assert response.status_code == 200

class ModelTestCase(TestCase):
    """
    tests for all Model in invest application
    """
    def setUp(self):
        user_a = User.objects.create_user(username='usr', password='User_password', email='usr@example.com')
        user_a.is_superuser = True
        self.user_a = user_a
        user_b = User.objects.create_user(username='usr1', password='User_password1', email='usr1@example.com')
        self.user_b = user_b

    def test_stock(self):
        Stock.objects.create(stock_name='stock_a', stock_long_name="stock_aaaaaa")
        stock_count = Stock.objects.all().count()
        self.assertEqual(stock_count, 1)
        self.assertNotEqual(stock_count, 0)

    def test_company(self):
        Company.objects.create(name="Coderslab",
                                 short_name ='CDL',
                                 stock ='GPW',
                                 description="Coderslab is an IT programming school",
                                 history="Company was founded in 2010",
                                 )
        company_count = Company.objects.all().count()
        self.assertEqual(company_count, 1)
        self.assertNotEqual(company_count, 0)


    def test_indicator(self):
        Indicator.objects.create(name="Indicator_1",
                                 short_name ='IND1',
                                 definition  ='Indicator_1 helps to indicate.',
                                 )
        indicator_count = Indicator.objects.all().count()
        self.assertEqual(indicator_count, 1)
        self.assertNotEqual(indicator_count, 0)

    def test_strategy(self):
        Strategy.objects.create(name="Strategy_1",
                                 indicator ='Best_indicator',
                                 description  ='The best strategy to invet ever.',
                                 )
        strategy_count = Strategy.objects.all().count()
        self.assertEqual(strategy_count, 1)
        self.assertNotEqual(strategy_count, 0)

    def test_subscription(self):
        Subscription.objects.create(email="subscriber1@example.com",
                                 )
        subscription_count = Subscription.objects.all().count()
        self.assertEqual(subscription_count, 1)
        self.assertNotEqual(subscription_count, 0)



class ViewsTestCase(TestCase):
    """
    tests for all views in invest application
    """

    def test_indexview(self):
        response = self.client.get(reverse('index'), {'car': 'car'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
