# Generated by Django 4.1.1 on 2022-09-24 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0085_remove_apl_bashinji_remove_apl_birinji_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundes_liga',
            name='bashinji',
        ),
        migrations.RemoveField(
            model_name='bundes_liga',
            name='birinji',
        ),
        migrations.RemoveField(
            model_name='bundes_liga',
            name='dordunji',
        ),
        migrations.RemoveField(
            model_name='bundes_liga',
            name='ikinji',
        ),
        migrations.RemoveField(
            model_name='bundes_liga',
            name='uchunji',
        ),
        migrations.RemoveField(
            model_name='cl',
            name='bashinji',
        ),
        migrations.RemoveField(
            model_name='cl',
            name='birinji',
        ),
        migrations.RemoveField(
            model_name='cl',
            name='dordunji',
        ),
        migrations.RemoveField(
            model_name='cl',
            name='ikinji',
        ),
        migrations.RemoveField(
            model_name='cl',
            name='uchunji',
        ),
        migrations.RemoveField(
            model_name='laliga',
            name='bashinji',
        ),
        migrations.RemoveField(
            model_name='laliga',
            name='birinji',
        ),
        migrations.RemoveField(
            model_name='laliga',
            name='dordunji',
        ),
        migrations.RemoveField(
            model_name='laliga',
            name='ikinji',
        ),
        migrations.RemoveField(
            model_name='laliga',
            name='uchunji',
        ),
        migrations.RemoveField(
            model_name='league1',
            name='bashinji',
        ),
        migrations.RemoveField(
            model_name='league1',
            name='birinji',
        ),
        migrations.RemoveField(
            model_name='league1',
            name='dordunji',
        ),
        migrations.RemoveField(
            model_name='league1',
            name='ikinji',
        ),
        migrations.RemoveField(
            model_name='league1',
            name='uchunji',
        ),
        migrations.RemoveField(
            model_name='seria_a',
            name='bashinji',
        ),
        migrations.RemoveField(
            model_name='seria_a',
            name='birinji',
        ),
        migrations.RemoveField(
            model_name='seria_a',
            name='dordunji',
        ),
        migrations.RemoveField(
            model_name='seria_a',
            name='ikinji',
        ),
        migrations.RemoveField(
            model_name='seria_a',
            name='uchunji',
        ),
        migrations.DeleteModel(
            name='jem',
        ),
    ]
