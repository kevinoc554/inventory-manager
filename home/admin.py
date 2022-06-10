from django.contrib import admin
from .models import Inventory


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'quantity',
        'unit_price',
    )

admin.site.register(Inventory)
