# Generated by Django 4.1.1 on 2022-09-24 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0028_alter_cl_bashinji_alter_cl_dordunji_alter_cl_ikinji_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cl',
            name='belli',
        ),
        migrations.AddField(
            model_name='cl',
            name='birinji',
            field=models.OneToOneField(default='win', on_delete=django.db.models.deletion.CASCADE, related_name='birinji', to='turkmenfutbol.jem'),
        ),
        migrations.AddField(
            model_name='cl',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]