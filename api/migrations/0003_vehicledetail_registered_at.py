# Generated by Django 3.0.5 on 2020-04-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200419_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicledetail',
            name='registered_at',
            field=models.DateTimeField(null=True),
        ),
    ]
