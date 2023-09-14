from django.shortcuts import render
from django.http import HttpResponse
def index_view(requests):
    return render(requests,'index.html')
def about_view(requests):
    return render(requests,'about.html')
def contact_view(requests):
    return render(requests,'contact.html')
# Create your views here.
