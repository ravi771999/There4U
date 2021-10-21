from django.contrib import admin

from order_api.models import Order
from order_api.models import Order_Detail


admin.site.register(Order)
admin.site.register(Order_Detail)
