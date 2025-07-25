from dal import autocomplete
from references.models import Status, Type, Category, Subcategory

class StatusAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Status.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

class TypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Type.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.all()
        type_id = self.forwarded.get('type', None)
        if type_id:
            qs = qs.filter(type_id=type_id)
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

class SubcategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Subcategory.objects.all()
        category_id = self.forwarded.get('category', None)
        if category_id:
            qs = qs.filter(category_id=category_id)
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs
