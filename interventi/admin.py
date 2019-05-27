from django.contrib import admin
from django.contrib.auth.models import User

from .models import (
    Fornitore, Intervento, InterventoAllegato, PuntoVendita,
)


class InterventoAllegatoInline(admin.TabularInline):
    model = InterventoAllegato
    verbose_name_plural = 'File Allegati'
    extra = 0


class FornitoreAdmin(admin.ModelAdmin):
    """
    Custom Fornitore admin class
    """
    list_display = (
        'nome', 'tipo_servizio_offerto', 'citta', 'referente', 'email', 'telefono',
    )
    ordering = (
        'nome',
    )
    list_filter = (
        'citta', 'referente',
    )
    search_fields = (
        'nome', 'citta', 'referente',
    )


class InterventoAdmin(admin.ModelAdmin):
    """
    Custom Intervento admin class
    """
    inlines = (
        InterventoAllegatoInline,
    )
    list_display = (
        'titolo', 'punto_vendita', 'segnalatore',
        'data_inserimento', 'data_ultima_modifica',
    )
    ordering = (
        '-data_inserimento',
    )
    list_filter = (
        ('punto_vendita', admin.RelatedOnlyFieldListFilter),
        'segnalatore',
        'data_inserimento', 'data_ultima_modifica',
    )
    search_fields = (
        'titolo', 'segnalatore',
    )


class InterventoAllegatoAdmin(admin.ModelAdmin):
    """
    Custom InterventoAllegato admin class
    """
    list_display = (
        'file_name', 'file_size_kb', 'data_inserimento',
        'titolo_intervento', 'punto_vendita_intervento',
    )
    ordering = (
        '-data_inserimento',
    )
    list_filter = (
        'data_inserimento',
        ('intervento__punto_vendita', admin.RelatedOnlyFieldListFilter),
        ('intervento', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = (
        'file',
    )

    def titolo_intervento(self, obj):
        return obj.intervento.titolo

    def punto_vendita_intervento(self, obj):
        return obj.intervento.punto_vendita


class PuntoVenditaAdmin(admin.ModelAdmin):
    """
    Custom PuntoVendita admin class
    """
    list_display = (
        'nome', 'citta', 'responsabile', 'email', 'telefono',
    )
    ordering = (
        'nome',
    )
    list_filter = (
        'citta', 'responsabile',
    )
    search_fields = (
        'nome', 'citta', 'responsabile',
    )


class FornitoreInline(admin.TabularInline):
    model = Fornitore
    # can_delete = True
    verbose_name_plural = 'fornitori'


admin.site.register(Fornitore, FornitoreAdmin)
admin.site.register(Intervento, InterventoAdmin)
admin.site.register(InterventoAllegato, InterventoAllegatoAdmin)
admin.site.register(PuntoVendita, PuntoVenditaAdmin)
