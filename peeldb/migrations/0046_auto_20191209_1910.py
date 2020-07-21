# Generated by Django 2.2.8 on 2019-12-09 19:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0045_auto_20181031_1054"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="searchresult",
            name="search_text",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="skill",
            name="meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
