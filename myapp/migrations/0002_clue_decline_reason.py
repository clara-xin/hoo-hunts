# Generated by Django 4.2.5 on 2023-11-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='decline_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
