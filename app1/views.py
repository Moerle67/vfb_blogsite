from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request):
   print(request)
   context = {
            'name' : 'Klaus Apfelbaum',
            'ort' : 'VFB-Ludwigsburg',
            'datum' : datetime.now(),
              }
   return render(request, 'app1/start.html', context) 
