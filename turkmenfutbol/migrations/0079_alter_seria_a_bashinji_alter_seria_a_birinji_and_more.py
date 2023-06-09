# Generated by Django 4.1.1 on 2022-09-24 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0078_alter_laliga_bashinji_alter_laliga_birinji_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seria_a',
            name='bashinji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='h', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='seria_a',
            name='birinji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='seria_a',
            name='dordunji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='g', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='seria_a',
            name='ikinji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='seria_a',
            name='uchunji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='f', to='turkmenfutbol.jem'),
        ),
    ]
