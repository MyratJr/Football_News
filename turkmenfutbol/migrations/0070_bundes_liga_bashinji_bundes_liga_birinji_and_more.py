# Generated by Django 4.1.1 on 2022-09-24 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0069_seria_a_bashinji_seria_a_birinji_seria_a_dordunji_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundes_liga',
            name='bashinji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='l', to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='bundes_liga',
            name='birinji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='bundes_liga',
            name='dordunji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='k', to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='bundes_liga',
            name='ikinji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i', to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='bundes_liga',
            name='uchunji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='j', to='turkmenfutbol.jem'),
        ),
    ]
