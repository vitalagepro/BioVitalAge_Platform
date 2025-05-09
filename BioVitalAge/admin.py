from django.contrib import admin
from .models import (
    UtentiRegistratiCredenziali,
    TabellaPazienti,
    RefertiCapacitaVitale,
    DatiEstesiRefertiCapacitaVitale,
    RefertiEtaBiologica,
    DatiEstesiRefertiEtaBiologica,
    RefertiEtaMetabolica,
    PrescrizioniEsami,
    Appointment,
    Resilienza,
    ValutazioneMS,
    TerapiaDomiciliare,
    TerapiaInStudio,
    AllegatiLaboratorio,
    AllegatiStrumentale
)

# --- Inline per i figli di TabellaPazienti ---
class PrescrizioniEsamiInline(admin.TabularInline):
    model = PrescrizioniEsami
    extra = 0
    fields = ("data_visita", "esami_prescritti")
    readonly_fields = ("data_visita",)

class TerapiaDomiciliareInline(admin.TabularInline):
    model = TerapiaDomiciliare
    extra = 0
    fields = ("farmaco", "assunzioni", "orari", "data_inizio", "data_fine")
    readonly_fields = ("data_inizio",)

class TerapiaInStudioInline(admin.TabularInline):
    model = TerapiaInStudio
    extra = 0
    fields = ("tipologia", "descrizione", "data_inizio", "data_fine")
    readonly_fields = ("data_inizio",)

class RefertiCapacitaVitaleInline(admin.TabularInline):
    model = RefertiCapacitaVitale
    extra = 0
    fields = ("data_referto", "punteggio")
    readonly_fields = ("data_referto",)

class RefertiEtaBiologicaInline(admin.TabularInline):
    model = RefertiEtaBiologica
    extra = 0
    fields = ("data_referto",)
    readonly_fields = ("data_referto",)

class RefertiEtaMetabolicaInline(admin.TabularInline):
    model = RefertiEtaMetabolica
    extra = 0
    fields = ("data_referto", "eta_metabolica")
    readonly_fields = ("data_referto",)

class ResilienzaInline(admin.TabularInline):
    model = Resilienza
    extra = 0
    fields = ("hrv", "risultato")

class ValutazioneMSInline(admin.TabularInline):
    model = ValutazioneMS
    extra = 0
    fields = ("frequenza_a_f", "tipo_a_f")

@admin.register(TabellaPazienti)
class TabellaPazientiAdmin(admin.ModelAdmin):
    list_display  = ("id", "name", "surname", "dob", "codice_fiscale")
    search_fields = ("name", "surname", "codice_fiscale")
    list_filter   = ("dob",)
    ordering      = ("surname", "name")
    inlines       = [
        PrescrizioniEsamiInline,
        TerapiaDomiciliareInline,
        TerapiaInStudioInline,
        RefertiCapacitaVitaleInline,
        RefertiEtaBiologicaInline,
        RefertiEtaMetabolicaInline,
        ResilienzaInline,
        ValutazioneMSInline,
    ]

# --- Admin standalone per i dottori ---
@admin.register(UtentiRegistratiCredenziali)
class UtentiRegistratiCredenzialiAdmin(admin.ModelAdmin):
    list_display  = ("user", "nome", "cognome", "email")
    search_fields = ("user__username", "nome", "cognome")

# --- Inline per l’estensione del referto VITALE ---
class DatiEstesiRefertiCapacitaVitaleInline(admin.StackedInline):
    model = DatiEstesiRefertiCapacitaVitale
    can_delete = False

@admin.register(RefertiCapacitaVitale)
class RefertiCapacitaVitaleAdmin(admin.ModelAdmin):
    list_display  = ("paziente", "data_referto", "punteggio")
    list_filter   = ("data_referto",)
    search_fields = ("paziente__name", "paziente__surname")
    inlines       = [DatiEstesiRefertiCapacitaVitaleInline]

# --- Inline per l’estensione del referto ETA BIOLOGICA ---
class DatiEstesiRefertiEtaBiologicaInline(admin.StackedInline):
    model = DatiEstesiRefertiEtaBiologica
    can_delete = False

@admin.register(RefertiEtaBiologica)
class RefertiEtaBiologicaAdmin(admin.ModelAdmin):
    list_display  = ("paziente", "data_referto")
    list_filter   = ("data_referto",)
    search_fields = ("paziente__name", "paziente__surname")
    inlines       = [DatiEstesiRefertiEtaBiologicaInline]

@admin.register(RefertiEtaMetabolica)
class RefertiEtaMetabolicaAdmin(admin.ModelAdmin):
    list_display  = ("paziente", "data_referto", "eta_metabolica")
    list_filter   = ("data_referto",)
    search_fields = ("paziente__name", "paziente__surname")

@admin.register(PrescrizioniEsami)
class PrescrizioniEsamiAdmin(admin.ModelAdmin):
    list_display  = ("paziente", "data_visita", "esami_prescritti")
    list_filter   = ("data_visita",)
    search_fields = ("paziente__name",)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display  = ("nome_paziente", "cognome_paziente", "data", "orario")
    list_filter   = ("data",)
    search_fields = ("nome_paziente", "cognome_paziente")

@admin.register(Resilienza)
class ResilienzaAdmin(admin.ModelAdmin):
    list_display  = ("paziente", "risultato")
    search_fields = ("paziente__name",)

@admin.register(ValutazioneMS)
class ValutazioneMSAdmin(admin.ModelAdmin):
    list_display  = ("paziente", "frequenza_a_f", "tipo_a_f")
    search_fields = ("paziente__name",)

@admin.register(AllegatiLaboratorio)
class AllegatiLaboratorioAdmin(admin.ModelAdmin):
    list_display  = ("paziente", "data_referto", "file", "created_at")
    list_filter   = ("data_referto",)
    search_fields = ("paziente__name", "paziente__surname")
    readonly_fields = ("created_at",)

@admin.register(AllegatiStrumentale)
class AllegatiStrumentaleAdmin(admin.ModelAdmin):
    list_display  = ("paziente", "data_referto", "file", "created_at")
    list_filter   = ("data_referto",)
    search_fields = ("paziente__name", "paziente__surname")
    readonly_fields = ("created_at",)
