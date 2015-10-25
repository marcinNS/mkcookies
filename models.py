from cms.models.pluginmodel import CMSPlugin

from django.db import models

class MKCookies(CMSPlugin):
    cookie_info = models.TextField(default='Nasz serwis używa plików cookie. Brak zmian ustawień przeglądarki oznacza zgodę na ich użycie.')
    cookie_url = models.URLField(max_length=200, null=True, blank=True)
    