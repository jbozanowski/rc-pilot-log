# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RCModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('rcmodel_type', models.CharField(default='heli', choices=[('heli', 'Helicopter'), ('multicopter', 'Multicopter'), ('acro', 'Airplane'), ('glider', 'Glider'), ('motoglider', 'Motor Glider')], verbose_name="Your RC Model's Type", max_length=64)),
                ('manufacturer', models.CharField(verbose_name='manufacturer', max_length=255)),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('owner', models.ForeignKey(verbose_name='Owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'RC Models',
                'verbose_name': 'RC Model',
            },
            bases=(models.Model,),
        ),
    ]
