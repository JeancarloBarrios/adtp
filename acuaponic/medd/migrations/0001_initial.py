# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
