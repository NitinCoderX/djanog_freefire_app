from django.apps import AppConfig


class AuthanticConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authantic'

    def ready(self):
        import authantic.signals
