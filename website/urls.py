

from django.urls import path
from. import views

urlpatterns = [
     path('home.html',views.home,name="home"),
     path('contact.html', views.contact, name="contact"),
    
     path('about.html', views.about, name="about"),
     path('news.html', views.news, name="news"),
     path('patients.html',views.patients, name="patients"),
     path('services.html', views.services, name="services"),
     path('appointment.html', views.appointment, name="appointment"),

]
