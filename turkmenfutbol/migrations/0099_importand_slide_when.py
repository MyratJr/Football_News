# Generated by Django 4.1.1 on 2022-09-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0098_alter_apl_maglumat1_alter_apl_maglumat2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='importand_slide',
            name='when',
            field=models.IntegerField(default=1),
        ),
    ]
