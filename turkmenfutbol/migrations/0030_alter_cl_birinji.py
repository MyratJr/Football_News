# Generated by Django 4.1.1 on 2022-09-24 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0029_remove_cl_belli_cl_birinji_cl_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cl',
            name='birinji',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='birinji', to='turkmenfutbol.jem'),
        ),
    ]