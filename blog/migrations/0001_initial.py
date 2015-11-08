# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField()),
                ('short_description', models.CharField(db_index=True, max_length=255)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(null=True, blank=True, default=None)),
                ('language', models.CharField(choices=[('pt-br', 'Portuguese'), ('en', 'English')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
