from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class ReciteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.word'

    def ready(self):
        autodiscover_modules('ttt')
