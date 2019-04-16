import os
from django.db import models
from django.urls import reverse 


class Restaurant(models.Model):
    """Model representing a restaurant."""
    name = models.CharField(max_length=200, help_text='Enter a restaurant (e.g. Waffle House)')
    menu = models.ManyToManyField('Food')
    cuisine = models.ManyToManyField('Cuisine')
    summary = models.CharField(max_length=200, help_text='Enter a short description about the restaurant (e.g. Quick late-night breakfast joint)')
    website = models.CharField(max_length=200, help_text='Enter a the official restaurant website (e.g. https://www.wafflehouse.com/)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this restaurant."""
        return reverse('restaurant-detail', args=[str(self.id)])
    
    def display_cuisine(self):
        """Create a string for the cuisine. This is required to display cuisine in Admin."""
        return ', '.join(cuisine.name for cuisine in self.cuisine.all()[:3])

    def display_menu(self):
        """Create a string for the menu. This is required to display menu in Admin."""
        return ', '.join(menu.name for menu in self.menu.all()[:3])

class Food(models.Model):
    """Model representing a food item."""
    name = models.CharField(max_length=200, help_text='Enter the food name (e.g. McDouble)')
    ingredients = models.ManyToManyField('Ingredient')
    allergens = models.ManyToManyField('Allergen')
    foodType = models.ForeignKey('foodType', on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this food."""
        return reverse('food-detail', args=[str(self.id)])

    def display_ingredients(self):
        """Create a string for the ingredients. This is required to display ingredients in Admin."""
        return ', '.join(ingredients.name for ingredients in self.ingredients.all()[:3])

    def display_allergens(self):
        """Create a string for the allergens. This is required to display allergens in Admin."""
        return ', '.join(allergens.name for allergens in self.allergens.all()[:3])

class Ingredient(models.Model):
    """Model representing  an ingredient."""
    name = models.CharField(max_length=200, help_text='Enter the ingredient name (e.g. Onion Powder)')
    ingredientType = models.ForeignKey('ingredientType', on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class foodType(models.Model):
    """Model representing the type of the food."""
    name = models.CharField(max_length=200, help_text='Enter the type of food (e.g. Burger)')
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class ingredientType(models.Model):
    """Model representing the type of the ingredient."""
    name = models.CharField(max_length=200, help_text='Enter the type of ingredient (e.g. Onion)')
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Cuisine(models.Model):
    """Model representing the cuisine."""
    name = models.CharField(max_length=200, help_text='Enter the cuisine (e.g. Mexican)')
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Allergen(models.Model):
    """Model representing an allergen, if any."""
    name = models.CharField(max_length=200, help_text='Enter an allergen, if any (e.g. Nuts)')
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name