from django.contrib import admin

# Register your models here.

from menu.models import Restaurant, Food, Ingredient, foodType, ingredientType, Cuisine, Allergen

# admin.site.register(Restaurant)
# Register the Admin classes for Restaurant using the decorator

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_menu', 'display_cuisine')
    fields = ['name', 'menu', 'cuisine']

# Register the admin class with the associated model
admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(foodType)
admin.site.register(ingredientType)
admin.site.register(Cuisine)
admin.site.register(Allergen)