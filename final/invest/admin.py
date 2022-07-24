from django.contrib import admin
from .models import Company, Stock, Indicator, Strategy, Subscription
# Register your models here.

admin.site.register(Company)
admin.site.register(Stock)
admin.site.register(Indicator)
admin.site.register(Strategy)
admin.site.register(Subscription)