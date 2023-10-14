# from django.db import models # Non spasial model
from django.contrib.gis.db import models # Spasial model

# Create your models here.
class Penjual(models.Model):
  nama = models.CharField(max_length=30, null=False, blank=False, unique=True)
  umur = models.IntegerField()
  perempuan = models.BooleanField(default=False)
  foto = models.ImageField(upload_to='foto_penjual', null=True, blank=False)

class Toko(models.Model):
  nama = models.CharField(max_length=50, unique=True)
  alamat = models.TextField()
  foto = models.ImageField(upload_to='foto_toko')
  lokasi = models.PointField(srid=4326, spatial_index=True)