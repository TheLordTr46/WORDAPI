from django.apps import AppConfig
from django.contrib.auth import get_user_model

class WordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'words'

    def ready(self):
        User = get_user_model()

        USERNAME = "admin"
        EMAIL = "admin@wordapi.com"
        PASSWORD = "Admin123!"

        try:
            if not User.objects.filter(username=USERNAME).exists():
                User.objects.create_superuser(
                    username=USERNAME,
                    email=EMAIL,
                    password=PASSWORD
                )
        except Exception:
            # migrate sırasında model henüz hazır olmayabilir
            pass
