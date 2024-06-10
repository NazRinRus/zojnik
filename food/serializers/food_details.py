from rest_framework import serializers
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
