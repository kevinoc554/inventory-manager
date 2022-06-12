import imp
from re import template
from django.shortcuts import render, redirect, get_object_or_404
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

def add_inventory(request):
    """
    A view to add items to the inventory
    """
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
    
    return redirect('home')

def delete_inventory(request, inventory_id):
    """
    A view to delete inventory items. Asks user to confirm 
    input as deletion cannot be undone. 
    """
    item = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == 'GET':
        template = 'home/delete.html'
        context = {
            'item': item,
        }

        return render(request, template, context)
