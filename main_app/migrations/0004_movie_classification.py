# Generated by Django 4.2.5 on 2023-11-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='classification',
            field=models.JSONField(default=dict),
        ),
    ]