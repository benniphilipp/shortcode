# Generated by Django 3.2 on 2023-09-08 08:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentpages', '0005_marketingfield_creator_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketingfield',
            name='creator_user',
        ),
        migrations.AlterField(
            model_name='marketingfield',
            name='headline',
            field=models.CharField(max_length=200, verbose_name='headline'),
        ),
        migrations.AlterField(
            model_name='marketingfield',
            name='subline',
            field=models.CharField(max_length=200, verbose_name='subline'),
        ),
        migrations.AlterField(
            model_name='marketingfield',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='text'),
        ),
    ]