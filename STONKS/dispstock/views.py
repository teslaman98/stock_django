from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
 

# Create your views here.

def home(request):
    return HttpResponse('Welcome')

def index(request):
    html = render_to_string('index.html', {})
    return HttpResponse(html)


