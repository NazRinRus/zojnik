from django.urls import path, include
from rest_framework.routers import DefaultRouter

from food.views.dicts import FoodCategoryView, TagView, AntitagView
from food.views.food_details import FoodView
from food.views.comments import CommentView

router = DefaultRouter()


router.register(r'', FoodView, 'foods')
router.register(r'(?P<pk>\d+)/comments', CommentView, 'comments')
router.register(r'dicts/foodcategory', FoodCategoryView, 'foodcategory')
router.register(r'dicts/tag', TagView, 'tag')
router.register(r'dicts/antitag', AntitagView, 'antitag')

urlpatterns = [
    # path('food/<int:pk>', FoodView.as_view(),
    #      name='foodret'),
    path('food/', include(router.urls)),
]

