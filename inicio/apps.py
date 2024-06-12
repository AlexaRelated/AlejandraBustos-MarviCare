from django.apps import AppConfig

class InicioConfig(AppConfig):
    name = 'inicio'

    def ready(self):
        # No realizar consultas a la base de datos
        pass
