# Generated by Django 4.1.1 on 2022-10-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0123_alter_league_logos_gysga'),
    ]

    operations = [
        migrations.AddField(
            model_name='football_news_continue',
            name='conf_l',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='football_news_continue',
            name='el',
            field=models.BooleanField(default=False),
        ),
    ]