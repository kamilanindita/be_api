from django.conf.urls import url
from django.urls import path, include
from .views import (
    ScrapApiView,
)

urlpatterns = [
    path('scrap', ScrapApiView.as_view()),
]