from django.db import models
from common.models.mixins import BaseDictModelMixin

def get_image_path(instance, file): # прописываю путь сохранения изображений, у каждого продукта своя папка
    return f'static/photos/food_img-{Food.objects.count()+1}/{file}'

class FoodCategory(BaseDictModelMixin):

    class Meta:
        verbose_name = 'Категория блюда'
        verbose_name_plural = 'Категории блюд'


class Tag(BaseDictModelMixin):

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Antitag(BaseDictModelMixin):

    class Meta:
        verbose_name = 'Антитэг'
        verbose_name_plural = 'Антитэги'


class Food(models.Model):
    name = models.CharField("Название блюда", max_length=255, null=False)
    calories = models.FloatField("Калории", null=True)
    protein = models.FloatField("Белки", null=True)
    fat = models.FloatField("Жиры", null=True)
    carbohydrates = models.FloatField("Углеводы", null=True)
    allergen = models.BooleanField("Содержит аллергены", default=True)
    other = models.TextField("Описание", null=True)
    category = models.ForeignKey(
        'FoodCategory', models.RESTRICT, 'food_category', verbose_name='Категория блюда'
    )
    tag = models.ManyToManyField(
        Tag, 'food_tag', blank=True, through='FoodTag'
    )
    antitag = models.ManyToManyField(
        Antitag, 'food_antitag', blank=True, through='FoodAntitag'
    )
    avatar = models.ImageField("Изображение блюда", upload_to=get_image_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'


class FoodTag(models.Model):
    food_id = models.ForeignKey(
        Food, models.PROTECT, 'foods', verbose_name='ID блюда'
    )
    tag_id = models.ForeignKey(
        Tag, models.PROTECT, 'tags', verbose_name='ID тега'
    )

    class Meta:
        verbose_name = 'Сводная таблица блюда и тэга'
        verbose_name_plural = 'Сводные таблицы блюд и тэгов'
        ordering = ('tag_id', 'food_id',)

    def __str__(self):
        return f'({self.pk}) {self.tag_id}'

class FoodAntitag(models.Model):
    food_id = models.ForeignKey(
        Food, models.PROTECT, 'foods_a', verbose_name='ID блюда'
    )
    antitag_id = models.ForeignKey(
        Antitag, models.PROTECT, 'antitags', verbose_name='ID тега'
    )

    class Meta:
        verbose_name = 'Сводная таблица блюда и тэга'
        verbose_name_plural = 'Сводные таблицы блюд и тэгов'
        ordering = ('antitag_id', 'food_id',)

    def __str__(self):
        return f'({self.pk}) {self.antitag_id}'
