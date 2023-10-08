"""
URL configuration for webgis_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from toko.views import faiz, home, about, penjual, Peta, input_penjual

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('faiz/', faiz),
    path('tentang/', about),
    path('penjual/', penjual, name='penjual'),
    path('peta/', Peta.as_view()),
    path('penjual/input/', input_penjual, name='form_input_penjual')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)