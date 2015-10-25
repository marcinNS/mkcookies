# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20150819_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='MKCookies',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('cookie_info', models.TextField(max_length=50, default='Nasz serwis używa plików cookie. Brak zmian ustawień przeglądarki oznacza zgodę na ich użycie.')),
                ('cookie_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
