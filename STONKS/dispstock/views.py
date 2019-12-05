from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from dispstock.app_graph import test
from dispstock.app_graph import dinky

# Create your views here.

def home(request):
    return HttpResponse('Welcome')

def index(request):
    return render(request, 'index.html',{'mess': dinky.STONKS_csv})


