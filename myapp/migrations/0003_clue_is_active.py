# Generated by Django 4.2.5 on 2023-11-12 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_clue_decline_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="clue",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
