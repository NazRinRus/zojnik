from rest_framework import serializers
from crum import get_current_user
from django.db import transaction
from rest_framework.exceptions import ParseError
from common.serializers.mixins import InfoModelSerializer, ExtendedModelSerializer
from food.models.food_details import FoodRating, Food
from users.serializers.users import UserShortSerializer
from food.serializers.food_details import FoodShortSerializer

class RatingShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodRating
        fields = (
            'id',
            'rating',
            'food_id',
            'user_id',
        )
class RatingListSerializer(InfoModelSerializer):
    food = FoodShortSerializer()
    user = UserShortSerializer()

    class Meta:
        model = FoodRating
        fields = (
            'id',
            'rating',
            'user',
            'food',
        )

class RatingRetrieveSerializer(InfoModelSerializer):
    food = FoodShortSerializer()
    user = UserShortSerializer()
    class Meta:
        model = FoodRating
        fields = (
            'id',
            'rating',
            'user',
            'food',
        )

class RatingCreateSerializer(ExtendedModelSerializer):
    food_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = FoodRating
        fields = (
            'id',
            'rating',
            'food_id',
            'user_id',
        )

    def validate(self, attrs):
        current_user = get_current_user()

        food_id = self.context['view'].kwargs.get('pk')
        food = Food.objects.filter(
            id=food_id,
        ).first()

        # Проверка, что блюдо есть
        if not food:
            raise ParseError(
                'Такого блюда нет.'
            )

        attrs['food'] = food

        return attrs

    # def create(self, validated_data):
    #     current_user = get_current_user()
    #     user_data = {
    #         'first_name': validated_data.pop('first_name'),
    #         'last_name': validated_data.pop('last_name'),
    #         'email': validated_data.pop('email'),
    #         'password': validated_data.pop('password'),
    #         'is_corporate_account': True,
    #     }
    #
    #     with transaction.atomic():
    #         user = User.objects.create_user(**user_data)
    #         validated_data['user'] = user
    #
    #         instance = super().create(validated_data)
    #     return instance

class RatingUpdateSerializer(ExtendedModelSerializer):

    class Meta:
        model = FoodRating
        fields = (
            'id',
            'rating',
            'food_id',
            'user_id',
        )

class RatingDeleteSerializer(ExtendedModelSerializer):

    class Meta:
        model = FoodRating
        fields = (
            'id',
            'rating',
            'food_id',
            'user_id',
        )

