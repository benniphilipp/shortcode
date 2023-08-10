# Generated by Django 3.2 on 2023-07-30 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortcode', '0016_alter_shortcodeclass_shortcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('short_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortcode.shortcodeclass')),
            ],
        ),
    ]