# Generated by Django 4.1.1 on 2022-09-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0010_result_alter_cl5_netije'),
    ]

    operations = [
        migrations.AddField(
            model_name='cl5',
            name='salam',
            field=models.CharField(default='25', max_length=35),
        ),
    ]
