from django.shortcuts import render

# Create your views here.
def resume_page(request):
    return render(request, 'Resume/resume.html')
def portfolio_page(request):
    return render(request, 'Portfolio/portfolio.html')