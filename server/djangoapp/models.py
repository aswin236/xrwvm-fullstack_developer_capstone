# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # optional additional fields
    country = models.CharField(max_length=100, blank=True)
    founded_year = models.IntegerField(blank=True, null=True)

    # string representation
    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:


class CarModel(models.Model):

    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey('CarMake', on_delete=models.CASCADE)

    # Dealer ID referring to Cloudant dealership
    dealer_id = models.IntegerField(blank=True, null=True)

    # Car model name
    name = models.CharField(max_length=100)

    # Car type choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')

    # Manufacturing year
    year = models.IntegerField(default=2023,
                               validators=[
                                   MaxValueValidator(2023),
                                   MinValueValidator(2015)
                               ])
    # Optional fields
    color = models.CharField(max_length=50, blank=True)
    horsepower = models.IntegerField(blank=True, null=True)

    # String representation
    def __str__(self):
        return self.name
