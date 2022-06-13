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
    inventory = Inventory.objects.filter(deleted=False)
    del_items = Inventory.objects.filter(deleted=True)
    inventory_form = InventoryForm()
    template = 'home/index.html'
    context = {
        'inventory': inventory,
        'del_items': del_items,
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
    if request.method == 'POST':
        item.deleted = True
        item.delete_comment = request.POST.get('delete-comment')
        item.save()
        return redirect('home')
    template = 'home/delete.html'
    context = {
        'item': item,
    }

    return render(request, template, context)


def edit_inventory(request, inventory_id):
    """
    A view to edit and update exisiting inventory items
    """
    item = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InventoryForm(instance=item)
    
    template = 'home/edit.html'
    context = {
        'item': item,
        'form': form,
    }
    return render(request, template, context)

def restore_inventory(request, inventory_id):
    """
    A view to restore deleted inventory items
    Returns item to current stock and removes delete comment
    """
    item = get_object_or_404(Inventory, pk=inventory_id)
    item.deleted = False
    item.delete_comment = ""
    item.save()
    return redirect('home')
