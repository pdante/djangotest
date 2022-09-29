# Generated by Django 4.1.1 on 2022-09-29 06:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_rename_id_rider_ride_rider_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US', unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('A', 'Admin'), ('R', 'Rider'), ('D', 'Driver')], max_length=1),
        ),
    ]
