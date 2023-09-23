# Generated by Django 3.2 on 2023-09-23 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkinbio', '0017_remove_linkinbio_links'),
        ('shortcode', '0028_shortcodeclass_button_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortcodeclass',
            name='linkinbiopage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='linkinbio.linkinbio'),
            preserve_default=False,
        ),
    ]