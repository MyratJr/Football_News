# Generated by Django 4.1.1 on 2022-09-24 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0074_remove_apl_birinji_apl_birinji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apl',
            name='ikinji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='a', to='turkmenfutbol.jem'),
        ),
    ]
