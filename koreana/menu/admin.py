from django.contrib import admin
from .models import FoodCategory, Food


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('description_ru', 'category', 'is_publish')
    list_editable = ['is_publish']


admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)
