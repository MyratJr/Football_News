# Generated by Django 4.1.1 on 2022-10-04 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0117_seria_a_maglumat1_seria_a_maglumat2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundes_liga',
            name='maglumat1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tt', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='bundes_liga',
            name='maglumat2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='yy', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='bundes_liga',
            name='maglumat3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='uu', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='bundes_liga',
            name='maglumat4',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ii', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='bundes_liga',
            name='maglumat5',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='oo', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='league1',
            name='maglumat1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='m', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='league1',
            name='maglumat2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='qq', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='league1',
            name='maglumat3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ww', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='league1',
            name='maglumat4',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ee', to='turkmenfutbol.subcategory'),
        ),
        migrations.AddField(
            model_name='league1',
            name='maglumat5',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rr', to='turkmenfutbol.subcategory'),
        ),
    ]