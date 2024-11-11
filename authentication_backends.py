from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailAuthBackend(ModelBackend):
    """
    Backend di autenticazione per effettuare il login tramite email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Cerca l'utente utilizzando l'email come identificativo
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None

        # Verifica la password
        if user.check_password(password):
            return user
        return None
