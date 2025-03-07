from django.shortcuts import render
from .models import Table

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'tables/table_list.html', {'tables': tables})

def available_tables(request):
    tables = Table.objects.filter(is_available=True)
    return render(request, 'tables/available_tables.html', {'tables': tables})

