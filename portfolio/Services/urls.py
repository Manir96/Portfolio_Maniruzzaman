from django.contrib import admin
from django.urls import path
from . import views as service


urlpatterns = [
    path('', service.service_page,name='service'),
    # path('store/', division.Division_Name_store,name='division_stor'),
    
    
]