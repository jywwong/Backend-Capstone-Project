from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    booking_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField (default=1, validators=[
            MaxValueValidator(6),
            MinValueValidator(1)
        ])
    booking_date = models.DateField()

class Menu(models.Model):
    menu_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'