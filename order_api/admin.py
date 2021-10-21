from django.contrib import admin

from order_api import models as orders_models


admin.site.register(orders_models.Order)
admin.site.register(orders_models.Order_Detail)

