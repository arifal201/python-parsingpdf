from django.urls import path
from . import views

urlpatterns = [
  path('', views.upload, name='index'),
  path('parsing-pdf', views.parsing_pdf, name='parsing-pdf')
]