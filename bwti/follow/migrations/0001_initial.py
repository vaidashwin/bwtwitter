# Generated by Django 2.1.7 on 2019-03-09 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BWTweeter',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('twitter_un', models.CharField(max_length=64, unique=True, verbose_name='Twitter Username')),
                ('tier', models.CharField(choices=[('OB', 'Official Blizzard'), ('TO', 'Tournaments'), ('DV', 'SC:R Developers'), ('CR', 'Casters'), ('PL', 'Players')], default='PL', max_length=2)),
            ],
        ),
    ]