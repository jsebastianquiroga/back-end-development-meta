from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    content = "<html><body><h1>Welcome to the Chefs Table</h1></body></html>"
    return HttpResponse(content)
