# Generated by Django 5.0.6 on 2024-06-27 02:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_alter_booking_id2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.users'),
        ),
    ]
