from drf_spectacular.utils import extend_schema_view, extend_schema
from food.models.food_details import Food
from food.serializers import food_details
from common.views.mixins import LCRUViewSet


@extend_schema_view(
    list=extend_schema(summary='Список блюд (Тэги и антитэги указываются в параметрах запроса и разделяются символом %,'
                               ' например: /api/food?tags=Мясо%Гарнир&antitags=Семена кунжута%Куркума%Паприка)', tags=['Блюда']),
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

    def get_queryset(self):
        if ('tags' in self.request.GET) and ('antitags' in self.request.GET):
            tags = self.request.GET['tags'].split('%')
            antitags = self.request.GET['antitags'].split('%')
            qs = Food.objects.prefetch_related(
                'tag',
                'antitag',
            ).filter(tag__name__in=tags).exclude(antitag__name__in=antitags)
        elif 'tags' in self.request.GET:
            tags = self.request.GET['tags'].split('%')
            qs = Food.objects.prefetch_related(
                'tag',
            ).filter(tag__name__in=tags)
        elif 'antitags' in self.request.GET:
            antitags = self.request.GET['antitags'].split('%')
            qs = Food.objects.prefetch_related(
                'antitag',
            ).exclude(antitag__name__in=antitags)
        else:
            qs = Food.objects.all()
        return qs


