# Generated by Django 3.0.5 on 2020-04-19 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renter',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='branch',
            name='created_on',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='renter',
            name='vehicles',
            field=models.ManyToManyField(related_name='renters', through='api.RenterVehicle', to='api.Vehicle'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vehicles', to='api.Branch'),
        ),
        migrations.AlterField(
            model_name='vehicledetail',
            name='vehicle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehicledetail', to='api.Vehicle'),
        ),
    ]
