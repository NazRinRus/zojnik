from drf_spectacular.utils import extend_schema_view, extend_schema
from food.models.food_details import FoodComment
from food.serializers import comments
from common.views.mixins import LCRUDViewSet


@extend_schema_view(
    list=extend_schema(summary='Список комментариев к блюду', tags=['Комментарии']),
    retrieve=extend_schema(summary='Комментарий', tags=['Комментарии']),
    create=extend_schema(summary='Создать комментарий', tags=['Комментарии']),
    update=extend_schema(summary='Изменить комментарий', tags=['Комментарии']),
    partial_update=extend_schema(summary='Изменить комментарий частично', tags=['Комментарии']),
    destroy=extend_schema(summary='Удалить комментарий', tags=['Комментарии']),
)
class CommentView(LCRUDViewSet):
    queryset = FoodComment.objects.all()
    serializer_class = comments.CommentCreateSerializer

    multi_serializer_class = {
        'list': comments.CommentListSerializer,
        'retrieve': comments.CommentRetrieveSerializer,
        'create': comments.CommentCreateSerializer,
        'update': comments.CommentUpdateSerializer,
        'partial_update': comments.CommentUpdateSerializer,
        'destroy': comments.CommentDeleteSerializer,
    }

    lookup_url_kwarg = 'comment_id'
    http_method_names = ('get', 'post', 'patch')

    def get_queryset(self):
        qs = FoodComment.objects.select_related(
            'user_id',
        ).prefetch_related(
            'food_id',
        )
        return qs


