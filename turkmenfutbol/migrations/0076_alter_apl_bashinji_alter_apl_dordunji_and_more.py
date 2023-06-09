# Generated by Django 4.1.1 on 2022-09-24 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0075_alter_apl_ikinji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apl',
            name='bashinji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='d', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='apl',
            name='dordunji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c', to='turkmenfutbol.jem'),
        ),
        migrations.AlterField(
            model_name='apl',
            name='uchunji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='b', to='turkmenfutbol.jem'),
        ),
    ]
