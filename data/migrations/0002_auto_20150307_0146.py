# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='assistantRefereeA',
            new_name='assistant_referee_a',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='assistantRefereeB',
            new_name='assistant_referee_b',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='headReferee',
            new_name='headr_eferee',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='scoreTeamA',
            new_name='score_team_b',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='scoreTeamB',
            new_name='scoret_eam_a',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='snitchReferee',
            new_name='snitch_referee',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='snitchRunner',
            new_name='snitch_runner',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='teamA',
            new_name='team_a',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='teamB',
            new_name='team_b',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='scoreType',
            new_name='score_type',
        ),
    ]
