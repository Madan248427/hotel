# Generated by Django 5.0.6 on 2024-06-20 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_remove_booking_id_booking_garden_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='garden_id',
            new_name='id',
        ),
    ]
