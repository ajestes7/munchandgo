import os
from django.db import models

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

class Food(models.Model):
    """Model representing a food item."""
    name = models.CharField(max_length=200, help_text='Enter the food name (e.g. McDouble)')
    ingredients = models.ManyToManyField('Ingredient')
    allergens = models.ManyToManyField('Allergen')
    foodType = models.ForeignKey('foodType', on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name

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