from django.contrib import admin
from shop.models import Category, Product, Favorite
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent')  # Показываем название и родительскую категорию
    search_fields = ('name',)  # Добавляем поиск по названию категорий

    class CategoryAdmin(DraggableMPTTAdmin):
        list_display = ('tree_actions', 'indented_title', 'parent')  # Показываем родителя

        class Media:
            js = ('admin/js/category_toggle.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Favorite)
