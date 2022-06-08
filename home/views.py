from re import template
from django.shortcuts import render


def home(request):
    """
    A view to render the tables listing the inventory and shipments,
    along with the forms to create new entries
    """
    template = 'home/index.html'
    context = {}

    return render(request, template, context)

