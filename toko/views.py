from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Penjual
from .forms import FormPenjual

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

class Peta(View):
  def get(self, request):
    # <view logic>
    # return HttpResponse("Peta dengan GET Method")
    dict_book = {
      'nama_buku': 'Novel Harry Potter Book 1',
      'penulis': 'JK Rowling',
      'negara_asal': 'Inggris'
    }

    list_kota = [
      'Jakarta', 'Surabaya',
      'Makassar', 'Medan',
      'Samarinda', 'Pontianak',
      'Ambon', 'Kupang',
      'Sorong', 'Jayapura'
    ]

    context = {
      'nama': 'faiz',
      'umur': 28,
      'perempuan': False,
      'buku': dict_book,
      'kota': list_kota
    }
    return render(request, 'peta.html', context)
  
def input_penjual(request):
  if request.method == 'POST':
    form = FormPenjual(request.POST)
    if form.is_valid():
      form.save()
      # return HttpResponse('Data anda valid, bisa diproses')
      return redirect('penjual')

  else:
    form = FormPenjual()
  
  context = {
    'form': form
  }
  return render(request, 'input_penjual.html', context)