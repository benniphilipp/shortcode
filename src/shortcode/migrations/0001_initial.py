# Generated by Django 3.2 on 2023-07-22 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortcodeClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_destination', models.CharField(max_length=520, unique=True)),
                ('url_titel', models.CharField(max_length=125, unique=True)),
                ('url_source', models.CharField(max_length=525, unique=True)),
                ('url_medium', models.CharField(max_length=525, unique=True)),
                ('url_campaign', models.CharField(max_length=525, unique=True)),
                ('url_term', models.CharField(max_length=525, unique=True)),
                ('url_content', models.CharField(max_length=525, unique=True)),
                ('url_tags', models.CharField(max_length=125, unique=True)),
                ('url_create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url_archivate', models.BooleanField(default=True)),
                ('url_active', models.BooleanField(default=False)),
                ('url_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]