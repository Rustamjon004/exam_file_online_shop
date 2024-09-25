from django.contrib import admin
from .models import Product, Comments

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id',  'new_price', 'name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['created_at']
    list_editable = ['new_price']
    list_per_page = 1

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'body']
    list_per_page = 1
    list_editable = ['body']

admin.site.register(Product, ProductAdmin)
admin.site.register(Comments,CommentsAdmin)