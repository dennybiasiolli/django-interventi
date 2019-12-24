from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PuntoVenditaViewSet,
)


# Create a router and register our viewsets with it.
ROUTER = DefaultRouter()
ROUTER.register('punti-vendita', PuntoVenditaViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(ROUTER.urls)),
]
