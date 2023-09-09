# Generated by Django 3.2 on 2023-09-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcode', '0027_alter_shortcodeclass_template_geo'),
        ('linkinbio', '0002_linkinbio_selected_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkinbio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='link_bio_images/'),
        ),
        migrations.AlterField(
            model_name='linkinbio',
            name='links',
            field=models.ManyToManyField(blank=True, null=True, to='shortcode.ShortcodeClass'),
        ),
        migrations.AlterField(
            model_name='linkinbio',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='link_bio_profile_images/'),
        ),
    ]
