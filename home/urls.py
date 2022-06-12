import imp
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_inventory, name="add_inventory"),
    path("delete/<int:inventory_id>", views.delete_inventory, name="delete_inventory"),
    path("edit/", views.edit_inventory, name="edit_inventory"),
]
