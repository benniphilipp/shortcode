# Generated by Django 3.2 on 2023-10-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20231029_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
