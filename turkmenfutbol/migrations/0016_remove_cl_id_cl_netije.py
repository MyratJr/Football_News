# Generated by Django 4.1.1 on 2022-09-24 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0015_remove_cl_netije_cl_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cl',
            name='id',
        ),
        migrations.AddField(
            model_name='cl',
            name='netije',
            field=models.OneToOneField(default=23, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='turkmenfutbol.result'),
        ),
    ]