from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("", views.home, name="home"),
    path("all-items", views.all_items, name="all-items"),
    path("all-categories", views.browse_by_category, name="all-categories"),
    path("category/<category>", views.list_by_category, name="list-by-category"),
    path("search/<keyword>", views.search_by_slug, name="search"),
    path("all-warehouses", views.browse_by_warehouse, name="all-warehouses"),
    path("warehouse/<warehouse>", views.list_by_warehouse, name="list-by-warehouse"),
    path("warehouse/<warehouse>/<filter>", views.list_by_warehouse_filter, name="list-by-warehouse-filter"),
    path("category/<category>/<filter>", views.list_by_category_filter, name="list-by-category-filter")
]