from django.contrib import admin
from .models import Shop, Item


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'name_length', 'address']
    list_display_links = ['name']

    def name_length(self, shop):
        return '{}글자'.format(len(shop.name))


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
