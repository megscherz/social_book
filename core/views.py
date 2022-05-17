from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # template_name = 'social_book/index.html'
    return render(request, 'index.html')