# Generated by Django 3.2 on 2023-10-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkinbio', '0018_auto_20231007_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlsocialprofiles',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
