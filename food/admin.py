from django.contrib import admin
from django.contrib.admin import TabularInline

from food.models import food_details, plate



##################################################
##### MODELS #####################################
##################################################

@admin.register(food_details.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calories', 'protein', 'fat', 'carbohydrates', 'allergen', 'other', 'category', 'avatar',)

@admin.register(food_details.FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)

@admin.register(food_details.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)

@admin.register(food_details.Antitag)
class AntitagAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)

@admin.register(plate.Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ('id', 'proteinproduct', 'garnishproduct', 'vegetableproduct',)