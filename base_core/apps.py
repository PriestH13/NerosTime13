from django.apps import AppConfig


class BaseCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_core'
