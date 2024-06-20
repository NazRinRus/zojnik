from rest_framework import serializers

from common.serializers.mixins import InfoModelSerializer, ExtendedModelSerializer
from food.models.plate import Plate
from food.serializers.food_details import FoodShortSerializer

class PlateShortSerializer(serializers.ModelSerializer):
    total_calories = serializers.FloatField()

    class Meta:
        model = Plate
        fields = (
            'id',
            'proteinproduct',
            'garnishproduct',
            'vegetableproduct',
            'total_calories',
        )
class PlateListSerializer(InfoModelSerializer):
    total_calories = serializers.FloatField()
    total_protein = serializers.FloatField()
    total_fat = serializers.FloatField()
    total_carbohydrates = serializers.FloatField()
    class Meta:
        model = Plate
        fields = (
            'id',
            'proteinproduct',
            'garnishproduct',
            'vegetableproduct',
            'total_calories',
            'total_protein',
            'total_fat',
            'total_carbohydrates',
        )

class PlateRetrieveSerializer(InfoModelSerializer):
    total_calories = serializers.FloatField()
    total_protein = serializers.FloatField()
    total_fat = serializers.FloatField()
    total_carbohydrates = serializers.FloatField()
    proteinproduct = FoodShortSerializer()
    garnishproduct = FoodShortSerializer()
    vegetableproduct = FoodShortSerializer()

    class Meta:
        model = Plate
        fields = (
            'id',
            'proteinproduct',
            'garnishproduct',
            'vegetableproduct',
            'total_calories',
            'total_protein',
            'total_fat',
            'total_carbohydrates',
        )

class PlateCreateSerializer(ExtendedModelSerializer):


    class Meta:
        model = Plate
        fields = (
            'id',
            'proteinproduct',
            'garnishproduct',
            'vegetableproduct',
        )


class PlateUpdateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Plate
        fields = (
            'id',
            'proteinproduct',
            'garnishproduct',
            'vegetableproduct',
        )

class PlateDeleteSerializer(ExtendedModelSerializer):

    class Meta:
        model = Plate
        fields = (
            'id',
            'proteinproduct',
            'garnishproduct',
            'vegetableproduct',
        )