from django.contrib import admin
# import models
from .models import Booking
from .models import Menu

# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)