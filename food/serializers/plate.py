from rest_framework import serializers

from common.serializers.mixins import InfoModelSerializer, ExtendedModelSerializer
from food.models.plate import Plate
from food.serializers.food_details import FoodShortSerializer

class PlateShortSerializer(serializers.ModelSerializer):

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
    proteinproduct = FoodShortSerializer()
    garnishproduct = FoodShortSerializer()
    vegetableproduct = FoodShortSerializer()
    total_calories = serializers.FloatField()
    total_protein = serializers.FloatField()
    total_fat = serializers.FloatField()
    total_carbohydrates = serializers.FloatField()
    allergen = serializers.BooleanField()
    total_price = serializers.FloatField()
    total_rating = serializers.FloatField()
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
            'allergen',
            'total_price',
            'total_rating',
        )

class PlateRetrieveSerializer(InfoModelSerializer):
    total_calories = serializers.FloatField()
    total_protein = serializers.FloatField()
    total_fat = serializers.FloatField()
    total_carbohydrates = serializers.FloatField()
    allergen = serializers.BooleanField()
    total_price = serializers.FloatField()
    proteinproduct = FoodShortSerializer()
    garnishproduct = FoodShortSerializer()
    vegetableproduct = FoodShortSerializer()
    total_rating = serializers.FloatField()

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
            'allergen',
            'total_price',
            'total_rating',
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