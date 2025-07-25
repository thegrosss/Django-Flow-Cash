from django.db import models
from references.models import Status, Type, Category, Subcategory

class FlowCash(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name="Тип")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name="Подкатегория")
    amount = models.FloatField(max_length=10, verbose_name="Сумма")
    comment = models.TextField(blank=True, verbose_name="Комментарий")

    class Meta:
        verbose_name = "Движение средств"
        verbose_name_plural = "Движения средств"

    def clean(self):
        if self.category and self.type and self.category.type_id != self.type_id:
            raise ValueError('Эта категория не принадлежит выбранному типу.')
        if self.subcategory and self.category and self.subcategory.category_id != self.category_id:
            raise ValueError('Эта подкатегория не принадлежит выбранной категории.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date}: {self.amount} руб."