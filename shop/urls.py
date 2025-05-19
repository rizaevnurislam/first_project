from django.urls import path
from shop.views import index_view, category_detail, product_detail, toggle_favorite, favorite_list, favorite_count_view, \
    search_view

app_name = "shop"

urlpatterns = [
    path('', index_view, name='index'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

    path('favorite/<int:product_id>/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', favorite_list, name='favorites'),
    path("favorite/count/", favorite_count_view, name="favorites_count"),
    path('search/', search_view, name='search'),


]
