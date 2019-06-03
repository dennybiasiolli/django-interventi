from rest_framework import serializers

from .models import (
    PuntoVendita
)


class PuntoVenditaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PuntoVendita
        fields = (
            'id', 'nome', 'indirizzo', 'citta', 'responsabile', 'email',
            'telefono', 'annotazioni'
        )
