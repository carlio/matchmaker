from django.contrib import admin

from .models import Instrument, Market, Order

admin.site.register(Instrument)
admin.site.register(Market)
admin.site.register(Order)
