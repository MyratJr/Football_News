# Generated by Django 4.1.1 on 2022-10-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0121_each_el_group_each_conferliga_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='league_logos',
            name='gysga',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
