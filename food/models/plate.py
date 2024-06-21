from django.db import models

from common.models.mixins import InfoMixin
from food.models import food_details

class Plate(InfoMixin):
    proteinproduct = models.ForeignKey(
        food_details.Food, models.RESTRICT, 'plate_protein', verbose_name='Протеиновое блюдо', null=True
    )
    garnishproduct = models.ForeignKey(
        food_details.Food, models.RESTRICT, 'plate_garnish', verbose_name='Гарнир', null=True
    )
    vegetableproduct = models.ForeignKey(
        food_details.Food, models.RESTRICT, 'plate_vegetable', verbose_name='Овощное блюдо', null=True
    )

    class Meta:
        verbose_name = 'Тарелка'
        verbose_name_plural = 'Тарелки'
        ordering = ('proteinproduct', 'garnishproduct', 'vegetableproduct',)

    def __str__(self):
        return f'({self.pk}) {self.proteinproduct} {self.garnishproduct} {self.vegetableproduct}'
