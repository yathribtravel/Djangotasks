
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact_as/',views.contact_as,name="contact_as"),
]
