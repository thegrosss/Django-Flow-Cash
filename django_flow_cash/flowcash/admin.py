from django.contrib import admin
from django import forms
from dal import autocomplete
from flowcash.models import FlowCash
from references.models import Type, Category, Subcategory, Status

class FlowCashAdminForm(forms.ModelForm):
    class Meta:
        model = FlowCash
        fields = '__all__'
        widgets = {
            'status': autocomplete.ModelSelect2(url='status-autocomplete'),
            'type': autocomplete.ModelSelect2(url='type-autocomplete'),
            'category': autocomplete.ModelSelect2(
                url='category-autocomplete',
                forward=['type']
            ),
            'subcategory': autocomplete.ModelSelect2(
                url='subcategory-autocomplete',
                forward=['category']
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ограничение категорий по выбранному типу
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                self.fields['category'].queryset = Category.objects.none()
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)
        else:
            self.fields['category'].queryset = Category.objects.all()

        # Ограничение подкатегорий по выбранной категории
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                self.fields['subcategory'].queryset = Subcategory.objects.none()
        elif self.instance.pk:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)
        else:
            self.fields['subcategory'].queryset = Subcategory.objects.all()

@admin.register(FlowCash)
class FlowCashAdmin(admin.ModelAdmin):
    form = FlowCashAdminForm
    list_display = ('date', 'type', 'category', 'subcategory', 'amount', 'status')
    list_filter = ('type', 'category', 'subcategory', 'status')
    search_fields = ('comment',)
    autocomplete_fields = ['status', 'type', 'category', 'subcategory']