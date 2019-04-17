from django.contrib import admin

# Register your models here.

from menu.models import Restaurant, Food, Ingredient, foodType, ingredientType, Cuisine, Allergen

# admin.site.register(Restaurant)
# Register the Admin classes for Restaurant using the decorator

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_menu', 'display_cuisine')
    fields = ['name', 'menu', 'cuisine', 'summary', 'website']

# Register the admin class with the associated model
admin.site.register(Restaurant, RestaurantAdmin)

# admin.site.register(Food)
# Register the Admin classes for Food using the decorator

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_ingredients', 'display_allergens', 'foodType')
    fields = ['name', 'ingredients', 'allergens', 'foodType']

# Register the admin class with the associated model
admin.site.register(Food, FoodAdmin)


# admin.site.register(Ingredient)
# Register the Admin classes for Food using the decorator

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredientType')
    fields = ['name', 'ingredientType']

# Register the admin class with the associated model
admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(foodType)
admin.site.register(ingredientType)
admin.site.register(Cuisine)
admin.site.register(Allergen)