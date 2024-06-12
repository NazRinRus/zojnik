from common.serializers.mixins import DictMixinSerializer
from food.models.food_details import FoodCategory, Tag, Antitag


class FoodCategorySerializer(DictMixinSerializer):
    class Meta:
        model = FoodCategory

class TagSerializer(DictMixinSerializer):
    class Meta:
        model = Tag

class AntitagSerializer(DictMixinSerializer):
    class Meta:
        model = Antitag