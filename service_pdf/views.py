from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import pdb
# Create your views here.
@csrf_protect
def upload(request):
  template = loader.get_template('upload.html')
  return HttpResponse(template.render())

@csrf_exempt
def parsing_pdf(request):
  if request.method == 'POST' and request.FILES['file_upload']:
    uploaded_file = request.FILES['file_upload']
    fs = FileSystemStorage()
    saved = fs.save(uploaded_file.name, uploaded_file)
    if saved:
      return HttpResponse(f"{settings.BASE_DIR}{settings.MEDIA_URL}")
  return HttpResponse("failed send request")