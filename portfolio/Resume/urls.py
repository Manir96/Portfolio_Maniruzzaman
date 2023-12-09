from django.contrib import admin
from django.urls import path
from . import views as resume


urlpatterns = [
    path('', resume.resume_page,name='resume'),
    path('portfolio', resume.portfolio_page,name='portfolio'),
    # path('store/', division.Division_Name_store,name='division_stor'),
    
    
]