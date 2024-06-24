from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.mixins import ListModelMixin
from django.db.models import Count, OuterRef, Sum, F, Q
from food.models.plate import Plate
from food.serializers import plate
from common.views.mixins import LCRUViewSet, LCRUDViewSet, ExtendedCRUAPIView, ExtendedGenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated


@extend_schema_view(
    list=extend_schema(summary='Список тарелок', tags=['Тарелки']),
    retrieve=extend_schema(summary='Тарелка детально', tags=['Тарелки']),
    create=extend_schema(summary='Создать тарелку', tags=['Тарелки']),
    update=extend_schema(summary='Изменить тарелку', tags=['Тарелки']),
    partial_update=extend_schema(summary='Изменить тарелку частично', tags=['Тарелки']),
)
class PlateView(LCRUViewSet):
    queryset = Plate.objects.all()
    serializer_class = plate.PlateCreateSerializer
    permission_classes = [AllowAny]

    multi_serializer_class = {
        'list': plate.PlateListSerializer,
        'retrieve': plate.PlateRetrieveSerializer,
        'create': plate.PlateCreateSerializer,
        'update': plate.PlateUpdateSerializer,
        'partial_update': plate.PlateUpdateSerializer,
    }

    http_method_names = ('get', 'post', 'patch')

    def get_queryset(self):
        qs = Plate.objects.prefetch_related(
            'proteinproduct',
            'garnishproduct',
            'vegetableproduct',
        ).annotate(
            total_calories= F('proteinproduct__calories') + F('garnishproduct__calories') + F('vegetableproduct__calories'),
            total_protein=F('proteinproduct__protein') + F('garnishproduct__protein') + F('vegetableproduct__protein'),
            total_fat=F('proteinproduct__fat') + F('garnishproduct__fat') + F('vegetableproduct__fat'),
            total_carbohydrates=F('proteinproduct__carbohydrates') + F('garnishproduct__carbohydrates') + F('vegetableproduct__carbohydrates'),
            allergen= Q(proteinproduct__allergen=True)|Q(garnishproduct__allergen=True)|Q(vegetableproduct__allergen=True),
            total_price=F('proteinproduct__price') + F('garnishproduct__price') + F('vegetableproduct__price'),
            total_rating=(F('proteinproduct__rating') + F('garnishproduct__rating') + F('vegetableproduct__rating'))/3,
        )
        return qs

