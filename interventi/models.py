from django.contrib.auth.models import User
from django.db import models


class Fornitore(models.Model):
    """
    Modello contenente i dati di ogni fornitore
    """
    nome = models.CharField(max_length=250)
    tipo_servizio_offerto = models.CharField(max_length=200)
    indirizzo = models.CharField(blank=True, max_length=250)
    citta = models.CharField(blank=True, max_length=200)
    referente = models.CharField(blank=True, max_length=200)
    email = models.EmailField(blank=True, max_length=200)
    telefono = models.CharField(blank=True, max_length=200)
    annotazioni = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Fornitori'

    def __str__(self):
        return f'{self.tipo_servizio_offerto} - {self.nome}'


class PuntoVendita(models.Model):
    """
    Modello contenente i dati di ogni punto vendita
    """
    nome = models.CharField(max_length=250)
    indirizzo = models.CharField(blank=True, max_length=250)
    citta = models.CharField(blank=True, max_length=200)
    regione = models.CharField(blank=True, max_length=200)
    responsabile = models.CharField(blank=True, max_length=200)
    email = models.EmailField(blank=True, max_length=200)
    telefono = models.CharField(blank=True, max_length=200)
    annotazioni = models.TextField(blank=True)
    fornitori_preferiti = models.ManyToManyField(
        Fornitore, blank=True, related_name='punti_vendita'
    )
    utenti_preferiti = models.ManyToManyField(
        User, blank=True, related_name='punti_vendita'
    )

    class Meta:
        verbose_name_plural = 'PuntiVendita'

    def __str__(self):
        return self.nome


class StatoInterventoCliente(models.Model):
    descrizione = models.CharField(max_length=250)
    ordine = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'StatiInterventoCliente'

    def __str__(self):
        return f'{self.ordine} - {self.descrizione}'


class StatoInterventoInterno(models.Model):
    descrizione = models.CharField(max_length=250)
    ordine = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'StatiInterventoInterno'

    def __str__(self):
        return f'{self.ordine} - {self.descrizione}'


class TipoIntervento(models.Model):
    descrizione = models.CharField(max_length=250)
    ordine = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'TipiIntervento'

    def __str__(self):
        return self.descrizione


class Intervento(models.Model):
    """
    Modello contenente i dati di ogni intervento
    """
    punto_vendita = models.ForeignKey(
        PuntoVendita, on_delete=models.CASCADE, related_name='interventi'
    )
    tipo_intervento = models.ForeignKey(
        TipoIntervento, on_delete=models.CASCADE, related_name='interventi',
        default=1
    )
    titolo = models.CharField(max_length=250)
    urgente = models.BooleanField(default=False)
    annotazioni = models.TextField(blank=True)
    segnalatore = models.CharField(blank=True, max_length=250)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_ultima_modifica = models.DateTimeField(auto_now=True)
    stato_cliente = models.ForeignKey(
        StatoInterventoCliente, on_delete=models.CASCADE,
        related_name='interventi', default=1
    )
    stato_interno = models.ForeignKey(
        StatoInterventoInterno, on_delete=models.CASCADE,
        related_name='interventi', default=1
    )

    class Meta:
        verbose_name_plural = 'Interventi'

    def __str__(self):
        return self.titolo


class InterventoAllegato(models.Model):
    """
    Modello relativo a un allegato della tabella interventi
    """
    intervento = models.ForeignKey(
        Intervento, on_delete=models.CASCADE, related_name='allegati',
    )
    file = models.FileField(
        upload_to='interventiAllegati/%Y/%m/%d/',
    )
    data_inserimento = models.DateTimeField(auto_now_add=True)

    def file_name(self):
        return self.file.name.split("/")[-1]

    def file_size_kb(self):
        return int(self.file.size/1024)

    class Meta:
        verbose_name_plural = 'InterventiAllegati'

    def __str__(self):
        return f'{self.file.name} ({self.file_size_kb()} KB)'


class InterventoCommento(models.Model):
    intervento = models.ForeignKey(
        Intervento, on_delete=models.CASCADE, related_name='commenti',
    )
    utente = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenti',
    )
    testo = models.TextField()
    data_inserimento = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'InterventiCommenti'

    def __str__(self):
        return f'{self.data_inserimento} - {self.utente}'


class Preventivo(models.Model):
    """
    Modello relativo ai preventivi di ogni intervento
    """
    intervento = models.ForeignKey(
        Intervento, related_name='preventivi', on_delete=models.CASCADE,
    )
    fornitore = models.ForeignKey(
        Fornitore, related_name='preventivi', on_delete=models.CASCADE
    )
    numero = models.CharField(max_length=50)
    is_confermato = models.BooleanField(default=False)
    data_inizio_lavori = models.DateField(blank=True, null=True)
    data_fine_lavori = models.DateField(blank=True, null=True)
    importo = models.DecimalField(
        blank=True, null=True,
        max_digits=15, decimal_places=2,
    )
    annotazioni = models.TextField(blank=True, null=True)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_ultima_modifica = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Preventivi'

    def __str__(self):
        return f'{self.numero} --> {self.fornitore.nome}'


class PreventivoAllegato(models.Model):
    """
    Modello relativo a un allegato della tabella preventivi
    """
    file = models.FileField(
        upload_to='preventivi/%Y/%m/%d/',
    )
    preventivo = models.ForeignKey(
        Preventivo, related_name='allegati', on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'PreventivoAllegati'

    def __str__(self):
        return f'{self.file.name} ({int(self.file.size/1024)} KB)'


class Scadenza(models.Model):
    """
    Modello relativo a una scadenza
    """
    data_scadenza = models.DateField()
    data_promemoria = models.DateField()
    descrizione = models.CharField(max_length=250)
    punto_vendita = models.ForeignKey(
        PuntoVendita, blank=True, null=True, on_delete=models.CASCADE,
        related_name='scadenze',
    )
    fornitore = models.ForeignKey(
        Fornitore, blank=True, null=True, on_delete=models.CASCADE,
        related_name='scadenze',
    )
    gestita = models.BooleanField()
    annotazioni = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Scadenze'

    def __str__(self):
        return f'{self.data_scadenza} - {self.descrizione}'


class ScadenzaAllegato(models.Model):
    """
    Modello relativo a un allegato della tabella preventivi
    """
    file = models.FileField(
        upload_to='scadenze/%Y/%m/%d/',
    )
    scadenza = models.ForeignKey(
        Scadenza, related_name='allegati', on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'ScadenzeAllegati'

    def __str__(self):
        return f'{self.file.name} ({int(self.file.size/1024)} KB)'
