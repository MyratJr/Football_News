# Generated by Django 4.1.1 on 2022-10-03 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0106_group_name_each_group_cl_related'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cl',
            name='related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turkmenfutbol.each_group'),
        ),
    ]