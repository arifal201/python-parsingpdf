from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.template.context_processors import csrf
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
      url_file = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
      return HttpResponse(f"{url_file}")
  return HttpResponse("failed send request")