# Generated by Django 3.0.5 on 2020-04-22 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200422_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vehicles', to='api.Branch'),
        ),
    ]
