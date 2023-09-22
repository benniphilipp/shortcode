# Generated by Django 3.2 on 2023-09-10 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkinbio', '0012_urlsocialprofiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlsocialprofiles',
            name='social_media_platform',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='linkinbio.socialmediaplatform'),
            preserve_default=False,
        ),
    ]