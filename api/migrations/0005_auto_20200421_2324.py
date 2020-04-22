# Generated by Django 3.0.5 on 2020-04-22 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200421_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vehicles', to='api.Color'),
            preserve_default=False,
        ),
    ]
