from django.urls import path
from . import views

urlpatterns = [
  path('home', views.home, name='homepage'),
  path('upload', views.upload, name='upload'),
  path('parsing-pdf', views.parsing_pdf, name='parsing-pdf')
]