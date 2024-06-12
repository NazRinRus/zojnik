from drf_spectacular.utils import extend_schema_view, extend_schema
from food.models.food_details import Food
from food.serializers import food_details
from common.views.mixins import LCRUViewSet


@extend_schema_view(
    list=extend_schema(summary='Список блюд', tags=['Блюда']),
    retrieve=extend_schema(summary='Блюдо детально', tags=['Блюда']),
    create=extend_schema(summary='Создать блюдо', tags=['Блюда']),
    update=extend_schema(summary='Изменить блюдо', tags=['Блюда']),
    partial_update=extend_schema(summary='Изменить блюдо частично', tags=['Блюда']),
)
class FoodView(LCRUViewSet):
    queryset = Food.objects.all()
    serializer_class = food_details.FoodCreateSerializer

    multi_serializer_class = {
        'list': food_details.FoodCreateSerializer,
        'retrieve': food_details.FoodRetrieveSerializer,
        'create': food_details.FoodCreateSerializer,
        'update': food_details.FoodUpdateSerializer,
        'partial_update': food_details.FoodUpdateSerializer,
    }

    http_method_names = ('get', 'post', 'patch')


