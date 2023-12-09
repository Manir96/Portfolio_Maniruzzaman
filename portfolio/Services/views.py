from django.shortcuts import render

# Create your views here.
def service_page(request):
    return render(request, 'Services/service.html')