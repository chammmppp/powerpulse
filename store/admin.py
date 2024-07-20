from django.contrib import admin
from .models import Store


# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}  # To make slug auto type from product_name
    list_display = ('product_name', 'price', 'stock', 'category', 'updated_date', 'is_available', 'is_trending')


admin.site.register(Store)
