# Generated by Django 4.1.1 on 2022-09-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0005_apl_g2_apl_g3_apl_g4_apl_g5'),
    ]

    operations = [
        migrations.CreateModel(
            name='last5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.ImageField(upload_to='last5')),
                ('lose', models.ImageField(upload_to='last5')),
                ('draw', models.ImageField(upload_to='last5')),
            ],
        ),
    ]