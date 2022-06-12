from dataclasses import fields
from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ('deleted', 'delete_comment')
