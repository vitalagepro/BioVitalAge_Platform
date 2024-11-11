# models.py
from django.db import models

class Utenti(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    data_registrazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Persona(models.Model):
    name = models.CharField(max_length=50 , null=True, blank=True)
    surname = models.CharField(max_length=50 , null=True, blank=True)
    dob = models.DateField(null=True, blank=True)  # Data di nascita
    gender = models.CharField(max_length=1, null=True, blank=True, choices=[('M', 'Male'), ('F', 'Female')])
    place_of_birth = models.CharField(max_length=100,null=True, blank=True)
    codice_fiscale = models.CharField(max_length=16, null=True, blank=True)

    # Calcolatore Età Biologica (temporaneamente nullable)
    chronological_age = models.IntegerField(null=True, blank=True)
    obri_index = models.FloatField(null=True, blank=True)
    d_roms = models.FloatField(null=True, blank=True)
    aa_epa = models.FloatField(null=True, blank=True)
    aa_dha = models.FloatField(null=True, blank=True)
    homa_test = models.FloatField(null=True, blank=True)
    cardiovascular_risk = models.FloatField(null=True, blank=True)
    osi = models.FloatField(null=True, blank=True)
    pat = models.FloatField(null=True, blank=True)

    # Risultati dei test sui globuli bianchi
    wbc = models.FloatField(null=True, blank=True)
    baso = models.FloatField(null=True, blank=True)
    eosi = models.IntegerField(null=True, blank=True)
    lymph = models.FloatField(null=True, blank=True)
    mono = models.FloatField(null=True, blank=True)
    neut = models.FloatField(null=True, blank=True)

    # Risultati dei test sui globuli rossi
    rbc = models.FloatField(null=True, blank=True)
    hct = models.FloatField(null=True, blank=True)
    hgb = models.FloatField(null=True, blank=True)
    mch = models.FloatField(null=True, blank=True)
    mchc = models.FloatField(null=True, blank=True)
    mcv = models.FloatField(null=True, blank=True)

    # Altri marker chiave
    glucose = models.FloatField(null=True, blank=True)
    creatinine = models.FloatField(null=True, blank=True)
    ferritin = models.FloatField(null=True, blank=True)
    albumin = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    bilirubin = models.FloatField(null=True, blank=True)
    uric_acid = models.FloatField(null=True, blank=True)

    biological_age = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"Persona ID: {self.id}"
