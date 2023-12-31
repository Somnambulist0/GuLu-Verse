# Generated by Django 4.2.5 on 2023-11-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_userprofile_bio_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('vote_average', models.FloatField()),
                ('release_date', models.DateField()),
            ],
        ),
    ]
