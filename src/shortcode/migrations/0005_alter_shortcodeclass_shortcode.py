# Generated by Django 3.2 on 2023-07-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcode', '0004_shortcodeclass_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcodeclass',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]