# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scoreTeamA', models.IntegerField()),
                ('scoreTeamB', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('scoreType', models.CharField(max_length=1, choices=[(b'H', b'Hoop'), (b'S', b'Snitch')])),
                ('game', models.ForeignKey(to='data.Game')),
                ('player', models.ForeignKey(to='data.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('league', models.ForeignKey(to='data.League')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='score',
            name='team',
            field=models.ForeignKey(to='data.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='team',
            field=models.ForeignKey(to='data.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='assistantRefereeA',
            field=models.ForeignKey(related_name='+', to='data.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='assistantRefereeB',
            field=models.ForeignKey(related_name='+', to='data.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='headReferee',
            field=models.ForeignKey(related_name='+', to='data.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='snitchReferee',
            field=models.ForeignKey(related_name='+', to='data.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='snitchRunner',
            field=models.ForeignKey(related_name='+', to='data.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='teamA',
            field=models.ForeignKey(related_name='gameA', to='data.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='teamB',
            field=models.ForeignKey(related_name='gameB', to='data.Team'),
            preserve_default=True,
        ),
    ]
