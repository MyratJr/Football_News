# Generated by Django 4.1.1 on 2022-09-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0014_result_remove_cl_id_cl_netije'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cl',
            name='netije',
        ),
        migrations.AddField(
            model_name='cl',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]