from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

def services(request):
    return render(request, 'services.html')

def freelancing(request):
    return render(request, 'freelancing.html')

# Add views for login/signup if needed.
