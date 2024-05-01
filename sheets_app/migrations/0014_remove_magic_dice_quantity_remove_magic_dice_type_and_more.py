# Generated by Django 5.0.3 on 2024-05-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets_app', '0013_alter_magic_dice_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magic',
            name='dice_quantity',
        ),
        migrations.RemoveField(
            model_name='magic',
            name='dice_type',
        ),
        migrations.AddField(
            model_name='magic',
            name='damage',
            field=models.CharField(default='', max_length=50),
        ),
    ]
