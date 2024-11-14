from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .utils import calculate_biological_age
from .models import Persona, Utenti
import logging
from django.contrib.auth.hashers import check_password, make_password
from django.db import connection
from django.db.models import Avg

# Debug del database in uso
print("Database in uso:", connection.settings_dict['NAME'])

# Configurazione del logger
logger = logging.getLogger(__name__)

# Vista per la pagina principale e il login
class MainPageView(View):
    def get(self, request):
        # Mostra la pagina di login
        return render(request, "includes/index.html")

    def post(self, request):
        # Recupera l'email e la password dal form
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            # Cerca l'utente nel database utilizzando l'email
            user = Utenti.objects.get(email=email)
            logger.info(f"Utente trovato: {user.email}")

            # Verifica la password
            if check_password(password, user.password):
                # Se la password è corretta, salva l'ID dell'utente nella sessione
                request.session['user_id'] = user.id
                logger.info("Login eseguito con successo")
                return redirect("home_page")  # Reindirizza alla homepage
            else:
                # Password errata, mostra un errore
                logger.warning("Password errata")
                return render(request, "includes/index.html", {"error": "Credenziali non valide"})
        
        except Utenti.DoesNotExist:
            # Utente non trovato, mostra un errore
            logger.warning("Utente non trovato")
            return render(request, "includes/index.html", {"error": "Credenziali non valide"})

class HomePageView(View):
    def get(self, request):
        # Controlla se l'utente è autenticato
        user_id = request.session.get('user_id')
        logger.info(f"ID utente nella sessione: {user_id}")

        if not user_id:
            return redirect('login')  # Reindirizza alla pagina di login se non autenticato

        # Recupera l'utente dal database
        try:
            user = Utenti.objects.get(id=user_id)
            logger.info(f"Nome utente recuperato: {user.nome}")
        except Utenti.DoesNotExist:
            logger.warning("Utente non trovato nel database")
            return redirect('login')

        # Recupera tutti i record di Persona per calcolare le medie
        records = Persona.objects.all()
        
        # Calcola le medie per l'età cronologica e biologica
        if records.exists():
            avg_chronological_age = records.aggregate(Avg('chronological_age'))['chronological_age__avg']
            avg_chronological_age = round(avg_chronological_age or 0)
            avg_biological_age = records.aggregate(Avg('biological_age'))['biological_age__avg']
            avg_biological_age = round(avg_biological_age or 0)       
        else:
            avg_chronological_age = avg_biological_age = None

        # Recupera gli ultimi cinque record
        recent_reports = records.order_by('-id')[:5]

        # Passa il nome dell'utente e i dati calcolati al template
        return render(request, "includes/homePage.html", {
            "user_name": user.nome,
            "avg_chronological_age": avg_chronological_age,
            "avg_biological_age": avg_biological_age,
            "recent_reports": recent_reports,
        })
# Vista per la pagina del calcolatore dell'età biologica
class CalcolatoreView(View):
    def get(self, request):
        return render(request, "includes/calcolatore.html")

    def post(self, request):
        # Raccoglie i dati dal form e li valida
        data = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'}
        
        try:
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


# Vista per la pagina dei risultati, che mostra tutti i record di Persona
class RisultatiView(View):
    def get(self, request):
        persone = Persona.objects.all()
        return render(request, "includes/risultati.html", {"persone": persone})

    def post(self, request):
        input_data = request.POST.get('inputField')
        persone = Persona.objects.filter(name__icontains=input_data) if input_data else Persona.objects.all()
        return render(request, "includes/risultati.html", {"persone": persone})


# Vista per il dettaglio di un singolo record di Persona
class PersonaDetailView(View):
    def get(self, request, id):
        persona = get_object_or_404(Persona, id=id)
        return render(request, "includes/persona_detail.html", {"persona": persona})
