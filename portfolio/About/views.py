from django.shortcuts import render

# Create your views here.

def about_page(request):
    return render(request, 'About/about.html')