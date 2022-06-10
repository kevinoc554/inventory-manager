import imp
from re import template
from django.shortcuts import render
from .models import Inventory
from .forms import InventoryForm


def home(request):
    """
    A view to render the tables listing the inventory and shipments,
    along with the forms to create new entries
    """
    inventory = Inventory.objects.all()
    inventory_form = InventoryForm()
    template = 'home/index.html'
    context = {
        'inventory': inventory,
        'inventory_form': inventory_form,
    }

    return render(request, template, context)

