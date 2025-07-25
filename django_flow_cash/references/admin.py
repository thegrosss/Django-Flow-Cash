from django.contrib import admin
from references.models import Status, Type, Category, Subcategory

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
