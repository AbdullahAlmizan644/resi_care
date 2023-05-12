# Generated by Django 4.1.3 on 2023-05-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_image_one', models.ImageField(upload_to='images/', verbose_name='My custom label')),
                ('poster_image_two', models.ImageField(upload_to='images/')),
                ('poster_image_three', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
