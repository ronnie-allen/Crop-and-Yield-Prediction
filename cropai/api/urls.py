from django.urls import path
from .views import crop_recommendation_view, yield_prediction_view

urlpatterns = [
    path('recommend-crop/', crop_recommendation_view),
    path('predict-yield/', yield_prediction_view),
]
