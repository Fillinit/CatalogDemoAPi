from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FoodCategory, Food, FoodSerializer, FoodListSerializer


class FoodCategoryView(APIView):
    def get(self, request):
        foods = Food.objects.filter(is_publish=True).values('category')
        set_category = set(id_category['category'] for id_category in list(foods))
        food_category = FoodCategory.objects.filter(pk__in=set_category)
        serializer = FoodListSerializer(food_category, many=True)
        return Response(serializer.data)
