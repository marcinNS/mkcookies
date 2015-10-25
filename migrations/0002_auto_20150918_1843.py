# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mkcookies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mkcookies',
            name='cookie_info',
            field=models.TextField(default='Nasz serwis używa plików cookie. Brak zmian ustawień przeglądarki oznacza zgodę na ich użycie.'),
            preserve_default=True,
        ),
    ]
