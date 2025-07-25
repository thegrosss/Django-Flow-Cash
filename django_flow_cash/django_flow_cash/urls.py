from django.urls import path
from django.contrib import admin
from references import autocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('status-autocomplete/', autocomplete.StatusAutocomplete.as_view(), name='status-autocomplete'),
    path('type-autocomplete/', autocomplete.TypeAutocomplete.as_view(), name='type-autocomplete'),
    path('category-autocomplete/', autocomplete.CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path('subcategory-autocomplete/', autocomplete.SubcategoryAutocomplete.as_view(), name='subcategory-autocomplete'),
]
