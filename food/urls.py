from django.urls import path, include
from rest_framework.routers import DefaultRouter

from food.views.dicts import FoodCategoryView, TagView, AntitagView

router = DefaultRouter()


router.register(r'dicts/foodcategory', FoodCategoryView, 'foodcategory')
router.register(r'dicts/tag', TagView, 'tag')
router.register(r'dicts/antitag', AntitagView, 'antitag')

urlpatterns = [
    path('food/', include(router.urls)),
]

