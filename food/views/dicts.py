from drf_spectacular.utils import extend_schema_view, extend_schema

from common.views.mixins import DictListMixin
from food.models.food_details import FoodCategory, Tag, Antitag


@extend_schema_view(
    list=extend_schema(summary='Категории продуктов', tags=['Словари']),
)
class FoodCategoryView(DictListMixin):
    model = FoodCategory

@extend_schema_view(
    list=extend_schema(summary='Тэги', tags=['Словари']),
)
class TagView(DictListMixin):
    model = Tag

@extend_schema_view(
    list=extend_schema(summary='Антитэги', tags=['Словари']),
)
class AntitagView(DictListMixin):
    model = Antitag