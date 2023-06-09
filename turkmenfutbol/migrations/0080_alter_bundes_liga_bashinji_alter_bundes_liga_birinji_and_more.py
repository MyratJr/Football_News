# Generated by Django 4.1.1 on 2022-09-24 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0079_alter_seria_a_bashinji_alter_seria_a_birinji_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundes_liga',
            name='bashinji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='l', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='bundes_liga',
            name='birinji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='bundes_liga',
            name='dordunji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='k', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='bundes_liga',
            name='ikinji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='bundes_liga',
            name='uchunji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='j', to='turkmenfutbol.jem'),
        ),
    ]
