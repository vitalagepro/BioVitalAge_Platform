from django.shortcuts import render, get_object_or_404
from django.views import View
from .utils import calculate_biological_age
from .models import Persona
import logging
from django.db import connection
print("Database in uso:", connection.settings_dict['NAME'])


logger = logging.getLogger(__name__)

class MainPageView(View):
    def get(self, request):
        return render(request, "includes/index.html")

    def post(self, request):
        print('working in progress')
        return render(request, "includes/index.html")


class HomePageView(View):
    def get(self, request):
        return render(request, "includes/homePage.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        logger.info(f"Username: {username}, Tentativo di login effettuato.")
        
        return render(request, "includes/homePage.html", {
            "username": username,
            "message": "Login tentativo eseguito"
        })


class CalcolatoreView(View):
    def get(self, request):
        return render(request, "includes/calcolatore.html")

    def post(self, request):
        data = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'}
        
        try:
            # Recupero e validazione dei dati dal form
            chronological_age = int(data.get('chronological_age'))
            obri_index = float(data.get('obri_index'))
            d_roms = float(data.get('d_roms'))
            aa_epa = float(data.get('aa_epa'))
            aa_dha = float(data.get('aa_dha'))
            homa_test = float(data.get('homa_test'))
            cardiovascular_risk = float(data.get('cardiovascular_risk'))
            osi = float(data.get('osi'))
            pat = float(data.get('pat'))
            
            glucose = float(data.get('glucose'))
            creatinine = float(data.get('creatinine'))
            ferritin = float(data.get('ferritin'))
            albumin = float(data.get('albumin'))
            protein = float(data.get('protein'))
            bilirubin = float(data.get('bilirubin'))
            uric_acid = float(data.get('uric_acid'))

            exams = [glucose, creatinine, ferritin, albumin, protein, bilirubin, uric_acid]

            # Calcolo dell'età biologica
            biological_age = calculate_biological_age(
                chronological_age, obri_index, d_roms, aa_epa, aa_dha,
                homa_test, cardiovascular_risk, osi, pat, exams
            )
            data['biological_age'] = biological_age

            # Salva i dati nel database
            persona = Persona.objects.create(**data)
            logger.info(f"Persona salvata nel database con ID: {persona.id}")

            context = {
                "show_modal": True,
                "biological_age": biological_age,
                "data": data,
            }
            return render(request, "includes/calcolatore.html", context)
        
        except Exception as e:
            logger.error(f"Errore durante l'inserimento dei dati: {e}")
            return render(request, "includes/calcolatore.html", {"error": "Si è verificato un errore durante il salvataggio."})


class RisultatiView(View):
    def get(self, request):
        # Recupera tutte le istanze di Persona
        persone = Persona.objects.all()
        return render(request, "includes/risultati.html", {"persone": persone})

    def post(self, request):
        # Filtro opzionale in base all'input dell'utente
        input_data = request.POST.get('inputField')
        persone = Persona.objects.filter(name__icontains=input_data) if input_data else Persona.objects.all()
        return render(request, "includes/risultati.html", {"persone": persone})


class PersonaDetailView(View):
    def get(self, request, id):
        persona = get_object_or_404(Persona, id=id)
        return render(request, "includes/persona_detail.html", {"persona": persona})
