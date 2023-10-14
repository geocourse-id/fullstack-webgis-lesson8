# from django.contrib import admin # Non Spasial admin
from django.contrib.gis import admin # Spasial admin
from .models import Penjual, Toko

# Register your models here.
admin.site.register(Penjual)

class TokoGeoAdmin(admin.GISModelAdmin):
  default_lon = -2
  default_lat = 110
  default_zoom = 5

admin.site.register(Toko, TokoGeoAdmin)