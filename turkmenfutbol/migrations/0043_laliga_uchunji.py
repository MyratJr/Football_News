# Generated by Django 4.1.1 on 2022-09-24 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0042_laliga_ikinji'),
    ]

    operations = [
        migrations.AddField(
            model_name='laliga',
            name='uchunji',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='uchunji2', to='turkmenfutbol.jem'),
            preserve_default=False,
        ),
    ]
