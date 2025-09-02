from django.urls import include, path


urlpatterns = [
    path("accounts/", include('api.user_api.urls')),
    path("cargos/", include('api.cargo_api.urls')),
]