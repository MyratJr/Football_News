# Generated by Django 4.1.1 on 2022-09-24 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0013_delete_cl5_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.CharField(max_length=10)),
                ('lose', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='cl',
            name='id',
        ),
        migrations.AddField(
            model_name='cl',
            name='netije',
            field=models.OneToOneField(default='salam', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='turkmenfutbol.result'),
            preserve_default=False,
        ),
    ]
