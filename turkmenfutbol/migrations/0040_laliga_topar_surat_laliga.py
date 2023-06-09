# Generated by Django 4.1.1 on 2022-09-24 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0039_remove_topar_surat_laliga_property_delete_laliga_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='laliga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='laliga_logos')),
                ('utuk', models.IntegerField(default=1)),
                ('oyun_jem', models.IntegerField()),
                ('utush', models.IntegerField()),
                ('dene_den', models.IntegerField()),
                ('utulush', models.IntegerField()),
                ('salnan_gol', models.IntegerField()),
                ('ozune_gol', models.IntegerField()),
                ('aratapawut', models.IntegerField()),
            ],
            options={
                'ordering': ['-utuk', '-aratapawut', '-salnan_gol', '-utush'],
            },
        ),
        migrations.CreateModel(
            name='topar_surat_laliga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='laliga_pictures')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turkmenfutbol.laliga')),
            ],
        ),
    ]
