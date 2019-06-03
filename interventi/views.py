from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import (
    PuntoVendita,
)
from .serializers import (
    PuntoVenditaSerializer,
)


class PuntoVenditaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PuntoVendita.objects.prefetch_related('utenti_preferiti')
    serializer_class = PuntoVenditaSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('$nome', '$citta', '$responsabile')
    pagination_class = None

    def get_queryset(self):
        if not self.request.user.is_staff:
            return self.queryset.filter(utenti_preferiti=self.request.user)
        return self.queryset
