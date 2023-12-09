from django.contrib import admin
from django.urls import path
from . import views as home


urlpatterns = [
    path('', home.home_page,name='home'),
    # path('store/', division.Division_Name_store,name='division_stor'),
    
    
]