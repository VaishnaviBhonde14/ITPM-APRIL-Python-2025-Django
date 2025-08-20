from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class productsAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','description','quantity')
    search_fields = ('id',)
