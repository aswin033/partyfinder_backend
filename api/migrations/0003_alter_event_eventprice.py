# Generated by Django 4.0.5 on 2023-01-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventPrice',
            field=models.IntegerField(),
        ),
    ]
