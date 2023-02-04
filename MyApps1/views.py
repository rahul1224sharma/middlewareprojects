from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show(request):
    print("added by view function")
    return HttpResponse('<h1>Custom Middleware </h1>')

def home_page_view(request):
	return HttpResponse('<h1> Hello This is from home page view </h1><hr />')