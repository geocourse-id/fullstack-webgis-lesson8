from django.forms import ModelForm
from .models import Penjual

class FormPenjual(ModelForm):
  class Meta:
    model = Penjual
    fields = ['nama', 'umur', 'perempuan', 'foto']