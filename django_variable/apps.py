from django.apps import AppConfig


class VariableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_variable'

    verbose_name = 'Configuración APP'

    def ready(self):
        import django_variable.signals