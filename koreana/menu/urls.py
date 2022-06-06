from django.urls import path
from . import views


app_name = 'foods'

urlpatterns = [
    path("foods/", views.FoodCategoryView.as_view()),
]