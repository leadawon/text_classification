from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('method', views.method),
    path('method_details', views.method_details),
    path('resume', views.resume),
    path('services', views.services),
]