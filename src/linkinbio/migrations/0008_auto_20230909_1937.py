# Generated by Django 3.2 on 2023-09-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkinbio', '0007_rename_titel_linkinbio_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmediaplatform',
            name='url',
        ),
        migrations.AddField(
            model_name='linkinbio',
            name='url_social',
            field=models.URLField(blank=True, null=True),
        ),
    ]
