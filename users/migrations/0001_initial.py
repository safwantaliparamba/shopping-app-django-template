# Generated by Django 4.0.6 on 2022-08-01 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('7e29797a-01e1-415c-83e4-5a0291ab4819'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=125)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('pin_code', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
