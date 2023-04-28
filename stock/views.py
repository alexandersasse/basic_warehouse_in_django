from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.

def home(request):
    return render(request, "stock/home.html")

def all_items(request):
    all_items_data = Item.objects.all()
    return render(request, "stock/all-items.html", {"all_items_data": all_items_data})

def browse_by_category(request):
    categories = []
    all_items_data = Item.objects.all()
    for item in all_items_data:
        if item.category not in categories:
            categories.append(item.category)
    return render(request, "stock/all-categories.html", {"categories": categories})

def list_by_category(request, category):
    all_items_data = Item.objects.all()
    all_states = []
    for item in all_items_data:
        if item.state not in all_states: all_states.append(item.state)
    return render(request, "stock/list-by-category.html", {"all_items_data": all_items_data, "category": category, "all_states": all_states})

def list_by_category_filter(request, category, filter):
    all_items_data = Item.objects.all()
    filtered_data = []
    for item in all_items_data:
        if str(item.category) == str(category) and str(item.state) == str(filter):
            filtered_data.append(item)
    return render(request, "stock/list-by-category-filter.html", {"filtered_data": filtered_data, "category": category, "filter": filter})


def search_by_slug(request, keyword):
    all_items_data = Item.objects.all()
    return render(request, "stock/search-result.html", {"all_items_data": all_items_data, "keyword": keyword})

def browse_by_warehouse(request):
    warehouses = []
    all_items_data = Item.objects.all()
    for item in all_items_data:
        if item.warehouse not in warehouses:
            warehouses.append(item.warehouse)
    return render(request, "stock/all-warehouses.html", {"warehouses": warehouses})

def list_by_warehouse(request, warehouse):
    all_items_data = Item.objects.all()
    filtered_data = []
    all_states = []
    for item in all_items_data:
        if item.state not in all_states: all_states.append(item.state)
        if str(item.warehouse) == str(warehouse):
            filtered_data.append(item)
    print(all_states)
    return render(request, "stock/list-by-warehouse.html", {"filtered_data": filtered_data, "all_states": all_states, "warehouse": warehouse})

def list_by_warehouse_filter(request, warehouse, filter):
    all_items_data = Item.objects.all()
    filtered_data = []
    for item in all_items_data:
        if str(item.warehouse) == str(warehouse) and str(item.state) == str(filter):
            filtered_data.append(item)
    return render(request, "stock/list-by-warehouse-filter.html", {"filtered_data": filtered_data, "warehouse": warehouse, "filter": filter})

