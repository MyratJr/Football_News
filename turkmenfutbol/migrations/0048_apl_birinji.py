# Generated by Django 4.1.1 on 2022-09-24 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0047_alter_laliga_birinji'),
    ]

    operations = [
        migrations.AddField(
            model_name='apl',
            name='birinji',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='turkmenfutbol.jem'),
            preserve_default=False,
        ),
    ]