import imp
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_inventory, name="add_inventory"),
    path("delete/<int:inventory_id>", views.delete_inventory, name="delete_inventory"),
    path("edit/<int:inventory_id>", views.edit_inventory, name="edit_inventory"),
    path("restore/<int:inventory_id>", views.restore_inventory, name="restore_inventory"),
]
