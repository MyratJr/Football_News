# Generated by Django 4.1.1 on 2022-09-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0071_league1_bashinji_league1_birinji_league1_dordunji_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apl',
            name='birinji',
        ),
        migrations.AddField(
            model_name='apl',
            name='birinji',
            field=models.ManyToManyField(null=True, related_name='z', to='turkmenfutbol.jem'),
        ),
    ]
