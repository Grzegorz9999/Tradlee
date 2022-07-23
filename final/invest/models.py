from django.db import models
from django.contrib.auth.models import User


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
    stock_names = models.ManyToManyField(Stock)
    description = models.TextField(null=True)
    history = models.TextField(null=True)

    def __str__(self):
        return self.name



#class indicator(models.Model):
 #   name = ForeignKey(Company, on_delete=models.CASCADE)



#class Company_rsi(models.Model):
 #   id = models.AutoField(primary_key=True)
  #  name_company = models.ForeignKey(Company, on_delete=models.CASCADE)
   # rsi =
