# Generated by Django 4.1.1 on 2022-09-24 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0064_apl_bashinji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laliga',
            name='birinji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='turkmenfutbol.jem'),
        ),
    ]
