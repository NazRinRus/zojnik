from rest_framework import serializers
from crum import get_current_user
from django.db import transaction
from rest_framework.exceptions import ParseError
from common.serializers.mixins import InfoModelSerializer, ExtendedModelSerializer
from food.models.food_details import FoodRating, Food
from users.serializers.users import UserShortSerializer
from food.serializers.food_details import FoodShortSerializer
from django.db.models import Avg

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
    food_id = FoodShortSerializer()
    user_id = UserShortSerializer()

    class Meta:
        model = FoodRating
        fields = (
            'id',
            'rating',
            'user_id',
            'food_id',
        )

    def to_representation(self, instance):
        food_id = int(self.context['view'].kwargs.get('pk'))
        if instance.food_id.pk == food_id:
            representation = super().to_representation(instance)
            return representation
        else:
            pass
            # representation = None

        # print('list_attrs:', instance, food_id, instance.food_id.pk)


    def validate(self, attrs):
        print('list_attrs:', attrs)
        return attrs

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
        food_id = int(self.context['view'].kwargs.get('pk'))
        food = Food.objects.filter(
            id=food_id,
        ).first()

        # Проверка, что блюдо есть
        if not food:
            raise ParseError(
                'Такого блюда нет.'
            )
        else:
            attrs['food_id'] = food

        attrs['user_id'] = current_user
        return attrs

    def create(self, validated_data):
        food = validated_data['food_id']
        # food = validated_data.pop('food')

        with transaction.atomic():

            instance = super().create(validated_data)

            rating = FoodRating.objects.filter(food_id=food.pk).aggregate(Avg('rating'))['rating__avg']
            food.rating = rating
            food.save()

        return instance
        # print('validated_data:', validated_data)
        # print('food_id:', food_id)
        # print('food (type):', food, ' (', type(food), ' )')
        # print('rating:', rating)
        # return validated_data

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

