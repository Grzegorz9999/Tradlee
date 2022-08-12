from django.db import models


# Create your models here.
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=64)
    stock_long_name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.stock_name


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=10)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    history = models.TextField(null=True)

    def __str__(self):
        return self.name


class Indicator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=10, null=True)
    definition = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Strategy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    indicator = models.ManyToManyField(Indicator)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254)
