# Generated by Django 4.1.2 on 2022-10-10 09:30

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_location_outlets_servicemen_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path),
        ),
        migrations.AddField(
            model_name='outlets',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path),
        ),
    ]
