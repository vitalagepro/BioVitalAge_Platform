# admin.py
from django.contrib import admin
from .models import Utenti, Persona

@admin.register(Utenti)
class UtentiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'data_registrazione')
    search_fields = ('nome', 'email')
    list_filter = ('data_registrazione',)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'surname', 'dob', 'gender', 'place_of_birth', 'codice_fiscale',
        'chronological_age', 'obri_index', 'd_roms', 'aa_epa', 'aa_dha', 'homa_test',
        'cardiovascular_risk', 'osi', 'pat', 'glucose', 'creatinine', 'ferritin', 
        'albumin', 'protein', 'bilirubin', 'uric_acid'
    )
    search_fields = ('name', 'surname', 'codice_fiscale', 'place_of_birth', 'dob')
    list_filter = ('gender', 'dob', 'chronological_age', 'cardiovascular_risk')

    fieldsets = (
        ('Patient Information', {
            'fields': ('name', 'surname', 'dob', 'gender', 'place_of_birth', 'codice_fiscale')
        }),
        ('Biological Age Calculator', {
            'fields': ('chronological_age', 'obri_index', 'd_roms', 'aa_epa', 'aa_dha', 
                       'homa_test', 'cardiovascular_risk', 'osi', 'pat')
        }),
        ('Blood Test Results - White Blood Cells', {
            'fields': ('wbc', 'baso', 'eosi', 'lymph', 'mono', 'neut')
        }),
        ('Blood Test Results - Red Blood Cells', {
            'fields': ('rbc', 'hct', 'hgb', 'mch', 'mchc', 'mcv')
        }),
        ('Other Key Markers', {
            'fields': ('glucose', 'creatinine', 'ferritin', 'albumin', 'protein', 
                       'bilirubin', 'uric_acid')
        }),
    )
