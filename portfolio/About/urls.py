from django.contrib import admin
from django.urls import path
from . import views as about


urlpatterns = [
    path('', about.about_page,name='about'),
    # path('store/', division.Division_Name_store,name='division_stor'),
    
    
]