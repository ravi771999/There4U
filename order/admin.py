from django.contrib import admin

from order import models as orders_models


admin.site.register(orders_models.Order)
admin.site.register(orders_models.Order_Detail)

