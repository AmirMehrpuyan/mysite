from django.shortcuts import render
from django.http import HttpResponse
def index_view(requests):
    return render(requests,'website/index.html')
def about_view(requests):
    return render(requests,'website/about.html')
def contact_view(requests):
    return render(requests,'website/contact.html')
# Create your views here.
