from django.contrib import admin

# Register your models here.
from .models import Covidiot, Zones

admin.site.register(Covidiot)
admin.site.register(Zones)