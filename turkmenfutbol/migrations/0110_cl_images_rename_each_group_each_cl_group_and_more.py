# Generated by Django 4.1.1 on 2022-10-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0109_alter_topar_surat_cl_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='CL_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='CL_pictures')),
            ],
        ),
        migrations.RenameModel(
            old_name='Each_Group',
            new_name='Each_CL_Group',
        ),
        migrations.DeleteModel(
            name='topar_surat_CL',
        ),
    ]
