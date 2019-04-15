from django.shortcuts import render

# Create your views here.
from menu.models import Restaurant, Food, Ingredient, foodType, ingredientType, Cuisine, Allergen

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_restaurant = Restaurant.objects.all().count()
    num_food = Food.objects.all().count()
    num_ingredient = Ingredient.objects.all().count()
    num_foodType = foodType.objects.all().count()
    num_ingredientType = ingredientType.objects.all().count()
    num_cuisine = Cuisine.objects.all().count()
    num_allergen = Allergen.objects.all().count()

    
    context = {
        'num_restaurant': num_restaurant,
        'num_food': num_food,
        'num_ingredient': num_ingredient,
        'num_foodType': num_foodType,
        'num_ingredientType': num_ingredientType,
        'num_cuisine': num_cuisine,
        'num_allergen': num_allergen,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class RestaurantListView(generic.ListView):
    model = Restaurant

class RestaurantDetailView(generic.DetailView):
    model = Restaurant
