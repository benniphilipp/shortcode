# Generated by Django 3.2 on 2023-09-09 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkinbio', '0006_auto_20230909_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkinbio',
            old_name='titel',
            new_name='title',
        ),
    ]