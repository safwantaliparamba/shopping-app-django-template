# Generated by Django 4.0.6 on 2022-08-01 11:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0132795f-3a58-478c-8408-07aed782cec1'), primary_key=True, serialize=False, unique=True),
        ),
    ]
