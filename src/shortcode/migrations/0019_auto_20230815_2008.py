# Generated by Django 3.2 on 2023-08-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcode', '0018_shortcodeclass_favicon_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='shortcodeclass',
            name='tags',
            field=models.ManyToManyField(related_name='shortcodes', to='shortcode.Tag'),
        ),
    ]
