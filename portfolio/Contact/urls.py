from django.contrib import admin
from django.urls import path
from . import views as contact


urlpatterns = [
    path('', contact.contact_page,name='contact'),
    # path('store/', division.Division_Name_store,name='division_stor'),
    
    
]