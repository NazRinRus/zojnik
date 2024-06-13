from drf_spectacular.utils import extend_schema_view, extend_schema
from food.models.food_details import FoodRating
from food.serializers import rating
from common.views.mixins import LCRUDViewSet


@extend_schema_view(
    list=extend_schema(summary='Список рейтингов к блюду', tags=['Рейтинг блюд']),
    retrieve=extend_schema(summary='Рейтинг', tags=['Рейтинг блюд']),
    create=extend_schema(summary='Оценить', tags=['Рейтинг блюд']),
    update=extend_schema(summary='Изменить оценку', tags=['Рейтинг блюд']),
    partial_update=extend_schema(summary='Изменить оценку частично', tags=['Рейтинг блюд']),
    destroy=extend_schema(summary='Удалить оценку', tags=['Рейтинг блюд']),
)
class RatingView(LCRUDViewSet):
    queryset = FoodRating.objects.all()
    serializer_class = rating.RatingCreateSerializer

    multi_serializer_class = {
        'list': rating.RatingListSerializer,
        'retrieve': rating.RatingRetrieveSerializer,
        'create': rating.RatingCreateSerializer,
        'update': rating.RatingUpdateSerializer,
        'partial_update': rating.RatingUpdateSerializer,
        'destroy': rating.RatingDeleteSerializer,
    }

    lookup_url_kwarg = 'rating_id'
    http_method_names = ('get', 'post', 'patch')

    def get_queryset(self):
        qs = FoodRating.objects.select_related(
            'user_id',
        ).prefetch_related(
            'food_id',
        )
        return qs


