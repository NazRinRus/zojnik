from rest_framework import serializers

from common.serializers.mixins import InfoModelSerializer, ExtendedModelSerializer
from food.models.food_details import Food

class FoodSerializer(serializers.ModelSerializer):

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