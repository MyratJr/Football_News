# Generated by Django 4.1.1 on 2022-09-24 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0070_bundes_liga_bashinji_bundes_liga_birinji_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='league1',
            name='bashinji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p', to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='league1',
            name='birinji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='league1',
            name='dordunji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='o', to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='league1',
            name='ikinji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m', to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='league1',
            name='uchunji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='n', to='turkmenfutbol.jem'),
        ),
    ]
