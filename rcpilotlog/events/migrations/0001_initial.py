# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rcmodels', '__first__'),
        ('batteries', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('event_type', models.CharField(verbose_name='event type', default='flight', choices=[('flight', 'Flight'), ('batt_charge', 'Battery charge'), ('batt_discharge', 'Battery discharge'), ('crash', 'Model crash'), ('maintenance', 'Craft maintenance')], max_length=128)),
                ('duration', models.IntegerField(verbose_name='duration', blank=True, null=True)),
                ('capacity_charged', models.PositiveIntegerField(verbose_name='capacity charged (in mAh)', blank=True, null=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('battery', models.ForeignKey(blank=True, verbose_name='battery', to='batteries.Battery', null=True)),
                ('rcmodel', models.ForeignKey(blank=True, verbose_name='RC model', to='rcmodels.RCModel', null=True)),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ('user', '-created'),
            },
            bases=(models.Model,),
        ),
    ]
