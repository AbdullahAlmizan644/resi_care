# Generated by Django 4.2.1 on 2023-05-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0011_rent_latitude_rent_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rent',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
