from rest_framework import serializers

from common.serializers.mixins import InfoModelSerializer, ExtendedModelSerializer
from food.models.food_details import FoodComment
from users.serializers.users import UserShortSerializer
from food.serializers.food_details import FoodShortSerializer

class CommentShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodComment
        fields = (
            'id',
            'comment',
            'food_id',
            'user_id',
        )
class CommentListSerializer(InfoModelSerializer):
    food = FoodShortSerializer()
    user = UserShortSerializer()

    class Meta:
        model = FoodComment
        fields = (
            'id',
            'comment',
            'user',
            'food',
        )

class CommentRetrieveSerializer(InfoModelSerializer):
    food = FoodShortSerializer()
    user = UserShortSerializer()
    class Meta:
        model = FoodComment
        fields = (
            'id',
            'comment',
            'user',
            'food',
        )

class CommentCreateSerializer(ExtendedModelSerializer):

    class Meta:
        model = FoodComment
        fields = (
            'id',
            'comment',
            'food_id',
            'user_id',
        )

class CommentUpdateSerializer(ExtendedModelSerializer):

    class Meta:
        model = FoodComment
        fields = (
            'id',
            'comment',
            'food_id',
            'user_id',
        )

class CommentDeleteSerializer(ExtendedModelSerializer):

    class Meta:
        model = FoodComment
        fields = (
            'id',
            'comment',
            'food_id',
            'user_id',
        )

