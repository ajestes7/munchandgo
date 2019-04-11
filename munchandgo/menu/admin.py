from django.contrib import admin

# Register your models here.

from menu.models import Restaurant, Food, Ingredient, foodType, ingredientType, Cuisine, Allergen

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(foodType)
admin.site.register(ingredientType)
admin.site.register(Cuisine)
admin.site.register(Allergen)