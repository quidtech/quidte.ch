# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150307_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='headr_eferee',
            new_name='head_referee',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='scoret_eam_a',
            new_name='score_team_a',
        ),
    ]
