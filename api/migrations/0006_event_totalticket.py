# Generated by Django 4.0.5 on 2023-01-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_event_eventdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='totalTicket',
            field=models.IntegerField(null=True),
        ),
    ]