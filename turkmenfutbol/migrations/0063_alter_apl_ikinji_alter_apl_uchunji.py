# Generated by Django 4.1.1 on 2022-09-24 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0062_apl_dordunji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apl',
            name='ikinji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='a', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='apl',
            name='uchunji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='b', to='turkmenfutbol.jem'),
        ),
    ]