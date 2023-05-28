# Generated by Django 4.1.1 on 2022-10-04 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0115_tkm_league_maglumat1_tkm_league_maglumat2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laliga',
            name='maglumat1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='h', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='laliga',
            name='maglumat2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='j', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='laliga',
            name='maglumat3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='k', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='laliga',
            name='maglumat4',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='l', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='laliga',
            name='maglumat5',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='z', to='turkmenfutbol.subcategory'),
        ),
    ]
