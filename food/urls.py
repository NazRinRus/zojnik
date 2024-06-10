from django.urls import path, include
from rest_framework.routers import DefaultRouter

from food.views.dicts import FoodCategoryView, TagView, AntitagView
from food.views.food_details import FoodView, FoodListView

router = DefaultRouter()


router.register(r'list', FoodListView, 'foodlist')
router.register(r'dicts/foodcategory', FoodCategoryView, 'foodcategory')
router.register(r'dicts/tag', TagView, 'tag')
router.register(r'dicts/antitag', AntitagView, 'antitag')

urlpatterns = [
    path('food/<int:pk>', FoodView.as_view(),
         name='foodret'),
    path('food/', include(router.urls)),
]

