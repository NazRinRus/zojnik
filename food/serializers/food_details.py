from rest_framework import serializers

from common.serializers.mixins import InfoModelSerializer, ExtendedModelSerializer
from food.models.food_details import Food

class FoodShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = (
            'id',
            'name',
        )
class FoodListSerializer(InfoModelSerializer):

    class Meta:
        model = Food
        fields = (
            'id',
            'name',
            'calories',
            'protein',
            'fat',
            'carbohydrates',
            'allergen',
            'other',
            'price',
            'rating',
            'avatar',
            'category',
            'rating',
        )

class FoodRetrieveSerializer(InfoModelSerializer):

    class Meta:
        model = Food
        fields = (
            'id',
            'name',
            'calories',
            'protein',
            'fat',
            'carbohydrates',
            'allergen',
            'other',
            'price',
            'rating',
            'avatar',
            'category',
            'rating',
        )

class FoodCreateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Food
        fields = (
            'id',
            'name',
            'calories',
            'protein',
            'fat',
            'carbohydrates',
            'allergen',
            'other',
            'price',
            'rating',
            'avatar',
            'category',
        )

class FoodUpdateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Food
        fields = (
            'id',
            'name',
            'calories',
            'protein',
            'fat',
            'carbohydrates',
            'allergen',
            'other',
            'price',
            'rating',
            'avatar',
            'category',
        )