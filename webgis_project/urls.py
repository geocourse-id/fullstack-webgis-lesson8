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
from toko.views import faiz, home, about, penjual, Peta, input_penjual, update_penjual, delete_penjual, webmap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('faiz/', faiz),
    path('tentang/', about, name='tentang'),
    path('penjual/', penjual, name='penjual'),
    path('testing/', Peta.as_view(), name='testing'),
    path('penjual/input/', input_penjual, name='form_input_penjual'),
    path('penjual/update/<int:pk>/', update_penjual, name='form_update_penjual'),
    path('penjual/delete/<int:pk>/', delete_penjual, name='form_delete_penjual'),
    path('webmap/', webmap)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)