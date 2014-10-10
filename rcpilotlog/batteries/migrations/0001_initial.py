# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('manufacturer', models.CharField(verbose_name='manufacturer', max_length=255)),
                ('capacity', models.PositiveIntegerField(verbose_name='capacity (in mAh)')),
                ('chemistry', models.CharField(choices=[('lipo', 'Lithium Polymer (LiPo)'), ('liion', 'Lithium-ion (Li-Ion)'), ('nicd', 'Nickel Cadmium (NiCd)')], verbose_name='chemistry', default='lipo', max_length=128)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('owner', models.ForeignKey(verbose_name='Owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Batteries',
                'verbose_name': 'Battery',
                'ordering': ['owner', 'name'],
            },
            bases=(models.Model,),
        ),
    ]
