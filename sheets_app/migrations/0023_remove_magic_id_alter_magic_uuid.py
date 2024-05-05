# Generated by Django 5.0.3 on 2024-05-05 18:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets_app', '0022_magic_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magic',
            name='id',
        ),
        migrations.AlterField(
            model_name='magic',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
