# Generated by Django 3.2 on 2023-09-17 10:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('linkinbio', '0014_alter_linkinbio_social_media_platforms'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkinbio',
            name='crate_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linkinbio',
            name='is_aktiv',
            field=models.BooleanField(default=True),
        ),
    ]
