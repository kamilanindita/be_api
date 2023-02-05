from django.conf.urls import url
from django.urls import path, include
from .views import (
    ScrapApiView,
    ScrappedTotalProductGrupBy
)

urlpatterns = [
    path('scrap', ScrapApiView.as_view()),
    path('scrapped/total', ScrappedTotalProductGrupBy.as_view())
]