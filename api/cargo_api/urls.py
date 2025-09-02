from django.urls import path
from .views import (
    RegionListAPIView, DistrictByRegionAPIView,
    CreateCargoAPIView, CreateLocationAPIView,
    GetDetailCargoAPIView
)


urlpatterns = [
    path('regions/', RegionListAPIView.as_view(), name='region-list'),
    path('districts/<int:region_id>', DistrictByRegionAPIView.as_view(), name='district-by-region'),
    path('create-cargo/', CreateCargoAPIView.as_view(), name='create-cargo'),
    path('create-location/', CreateLocationAPIView.as_view(), name='cargo-list'),
    path('<int:pk>', GetDetailCargoAPIView.as_view(), name='cargo-detail'),
]