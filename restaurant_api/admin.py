from django.contrib import admin

from restaurant_api.models import Restaurant_Menu
from restaurant_api.models import Restaurant
from restaurant_api.models import Ownership
from restaurant_api.models import Food
from restaurant_api.models import Menu
from restaurant_api.models import Menu_Food

admin.site.register(Restaurant_Menu)
admin.site.register(Restaurant)
admin.site.register(Ownership)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(Menu_Food)
