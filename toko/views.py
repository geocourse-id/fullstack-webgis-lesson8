from django.shortcuts import render
from django.http import HttpResponse
from .models import Penjual

# Create your views here.
def faiz(request):
  return HttpResponse('<h1>Hello World! Nama saya adalah Faiz</h1>')

def home(request):
  # return HttpResponse('<h1>Halaman Home</h1>')
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def penjual(request):
  data_penjual = Penjual.objects.all()
  # for data in data_penjual:
  #   print(data.nama, data.umur)
  context = {
    'penjual': data_penjual
  }
  return render(request, 'penjual.html', context)