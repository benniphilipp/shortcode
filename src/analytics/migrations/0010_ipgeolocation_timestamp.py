# Generated by Django 3.2 on 2023-08-17 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0009_alter_ipgeolocation_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipgeolocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]