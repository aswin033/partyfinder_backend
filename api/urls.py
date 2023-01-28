from django.urls import path

from api import views

urlpatterns = [
    path('cities/', views.getCity),
    path('addcity/', views.addCity),
    path('viewCity/', views.viewCity),
    path("deleteCity/", views.deleteCity),

     ##event paths##

     path('getEvents/', views.getEvents),
     path('addEvent/', views.addEvent),
     path('viewEvent/', views.viewEvent),
     path('deleteEvent/', views.deleteEvent),
]