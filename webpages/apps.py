print('-'*20, __file__, '-'*20)

from django.apps import AppConfig


class WebpagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webpages'

