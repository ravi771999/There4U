from django.contrib import admin

from restaurant import models as restaurant_models

admin.site.register(restaurant_models.Restaurant_Menu)
admin.site.register(restaurant_models.Restaurant)
admin.site.register(restaurant_models.Ownership)
admin.site.register(restaurant_models.Food)
admin.site.register(restaurant_models.Menu)
admin.site.register(restaurant_models.Menu_Food)
