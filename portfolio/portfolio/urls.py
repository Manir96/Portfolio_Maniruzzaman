from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('Home.urls')),
    path("about/",include('About.urls')),
    path("contact/",include('Contact.urls')),
    path("resume/",include('Resume.urls')),
    path("service/",include('Services.urls')),
]
