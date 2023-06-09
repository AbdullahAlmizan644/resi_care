# Generated by Django 3.2.7 on 2023-03-25 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_auth', '0004_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('division', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong')], max_length=50)),
                ('district', models.CharField(choices=[('Gec Moor', 'Gec Moor'), ('Chawkbazar', 'Chawkbazar'), ('mirpur', 'Mirpur'), ('Gulshan', 'Gulshan')], max_length=1000)),
                ('details_address', models.TextField()),
                ('teacher_details', models.TextField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
