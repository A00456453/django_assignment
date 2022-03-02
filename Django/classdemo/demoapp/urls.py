from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("hotels_list/", views.Hotels_list, name="hotelList"),
]