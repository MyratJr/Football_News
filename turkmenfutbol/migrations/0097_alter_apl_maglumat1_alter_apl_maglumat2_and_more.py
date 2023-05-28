# Generated by Django 4.1.1 on 2022-09-26 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turkmenfutbol', '0096_alter_apl_maglumat1_alter_apl_maglumat2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apl',
            name='maglumat1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='q', to='turkmenfutbol.last5'),
        ),
        migrations.AlterField(
            model_name='apl',
            name='maglumat2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='w', to='turkmenfutbol.last5'),
        ),
        migrations.AlterField(
            model_name='apl',
            name='maglumat3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='e', to='turkmenfutbol.last5'),
        ),
        migrations.AlterField(
            model_name='apl',
            name='maglumat4',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='r', to='turkmenfutbol.last5'),
        ),
        migrations.AlterField(
            model_name='apl',
            name='maglumat5',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='t', to='turkmenfutbol.last5'),
        ),
    ]
