# Generated by Django 4.1.1 on 2022-09-24 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0061_apl_uchunji'),
    ]

    operations = [
        migrations.AddField(
            model_name='apl',
            name='dordunji',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c', to='turkmenfutbol.jem'),
        ),
    ]