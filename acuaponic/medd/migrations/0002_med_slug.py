# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='med',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 11, 12, 5, 53, 17, 658795, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
