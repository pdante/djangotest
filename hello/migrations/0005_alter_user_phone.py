# Generated by Django 4.1.1 on 2022-09-29 10:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(help_text='format: xxx-xxx-xxxx', max_length=20, validators=[django.core.validators.RegexValidator('[1-9][0-9]{2}-[1-9][0-9]{2}-[0-9]{4}$')]),
        ),
    ]