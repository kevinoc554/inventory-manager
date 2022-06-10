import imp
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_inventory, name="add_inventory"),
]
