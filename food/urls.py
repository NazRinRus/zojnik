from django.urls import path, include
from rest_framework.routers import DefaultRouter

from food.views.dicts import FoodCategoryView, TagView, AntitagView
from food.views.food_details import FoodView
from food.views.plate import PlateView
from food.views.comments import CommentView
from food.views.rating import RatingView

router = DefaultRouter()


router.register(r'', FoodView, 'foods')
# router.register(r'plate', PlateView, 'plates')
router.register(r'(?P<pk>\d+)/comments', CommentView, 'comments')
router.register(r'(?P<pk>\d+)/rating', RatingView, 'rating')
router.register(r'dicts/foodcategory', FoodCategoryView, 'foodcategory')
router.register(r'dicts/tag', TagView, 'tag')
router.register(r'dicts/antitag', AntitagView, 'antitag')

urlpatterns = [
    path('plate/', PlateView.as_view({'get': 'list', 'post': 'create'}),
         name='plates'),
    path('plate/<int:pk>', PlateView.as_view({'get': 'retrieve'}),
         name='plate'),
    path('food/', include(router.urls)),
]

