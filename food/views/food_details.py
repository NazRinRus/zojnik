from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import RetrieveUpdateAPIView
from food.models.food_details import Food
from food.serializers import food_details
from common.views.mixins import ListViewSet


@extend_schema_view(
    get=extend_schema(summary='Блюдо', tags=['Блюда']),
    put=extend_schema(summary='Редактировать блюдо', tags=['Блюда']),
    patch=extend_schema(summary='Редактировать частично', tags=['Блюда']),
)
class FoodView(RetrieveUpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = food_details.FoodSerializer
    http_method_names = ('get', 'patch')

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return food_details.FoodSerializer
        return food_details.FoodSerializer

@extend_schema_view(
    list=extend_schema(summary='Список блюд', tags=['Блюда']),
)
class FoodListView(ListViewSet):
    queryset = Food.objects.all()
    serializer_class = food_details.FoodSerializer
