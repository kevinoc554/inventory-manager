from re import template
from django.shortcuts import render
from .models import Inventory


def home(request):
    """
    A view to render the tables listing the inventory and shipments,
    along with the forms to create new entries
    """
    inventory = Inventory.objects.all()
    template = 'home/index.html'
    context = {
        'inventory': inventory,
    }

    return render(request, template, context)

