# Generated by Django 5.0.3 on 2024-05-29 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns_app', '0014_alter_campaign_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='code',
            field=models.CharField(default='gdrktg8c', editable=False, max_length=8, unique=True),
        ),
    ]
