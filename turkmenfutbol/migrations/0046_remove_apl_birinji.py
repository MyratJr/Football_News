# Generated by Django 4.1.1 on 2022-09-24 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0045_apl_birinji'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apl',
            name='birinji',
        ),
    ]
