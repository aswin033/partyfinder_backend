# Generated by Django 4.0.5 on 2023-01-28 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_event_eventtype_alter_event_eventimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
