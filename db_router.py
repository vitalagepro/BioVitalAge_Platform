# db_router.py

class LoginRegisterRouter:
    """
    Un router per indirizzare i modelli della tabella LoginRegister al database LoginRegister.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'BioVitalAge_Login':
            return 'default'  # Il database LoginRegister è definito come 'default' in settings.py
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'BioVitalAge_Login':
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'BioVitalAge_Login':
            return db == 'default'
        return None


class MedicalRouter:
    """
    Un router per indirizzare i modelli della tabella Medical al database medical.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'medical_app':
            return 'medical_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'medical_app':
            return 'medical_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'medical_app':
            return db == 'medical_db'
        return None
