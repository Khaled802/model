from django.urls import path
from .views import SearchImage
urlpatterns = [
    path('image_search/', SearchImage.as_view()),
]