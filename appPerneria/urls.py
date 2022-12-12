from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
  path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
  path('admin/', admin.site.urls),
  path('', views.Inicio, name="home-page"),
  #Varios
  
]