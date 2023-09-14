from django.shortcuts import render
from django.http import HttpResponse
def index_view(requests):
    return HttpResponse('<h1>home</h1>')
def about_view(requests):
    return HttpResponse('<h1>about</h1>')
def contact_view(requests):
    return HttpResponse('<h1>contact</h1>')
# Create your views here.
