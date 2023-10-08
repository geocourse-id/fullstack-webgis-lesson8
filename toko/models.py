from django.db import models

# Create your models here.
class Penjual(models.Model):
  nama = models.CharField(max_length=30, null=False, blank=False, unique=True)
  umur = models.IntegerField()
  perempuan = models.BooleanField(default=False)