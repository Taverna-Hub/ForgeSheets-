# Generated by Django 5.0.3 on 2024-04-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets_app', '0003_alter_race_charisma_buff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='race',
            field=models.CharField(max_length=75),
        ),
    ]
