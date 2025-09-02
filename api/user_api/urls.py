from django.urls import path
from .views import RegisterUserAPIView, UserAPIView


urlpatterns = [
    path('register', RegisterUserAPIView.as_view()),
    path('user/<int:tg_id>', UserAPIView.as_view()),
]