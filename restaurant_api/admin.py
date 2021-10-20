from django.contrib import admin
from restaurant_api import models

admin.site.register(models.Restaurant_Menu)
admin.site.register(models.Restaurant)
admin.site.register(models.Ownership)
admin.site.register(models.Food)
admin.site.register(models.Menu)
admin.site.register(models.Menu_Food)
