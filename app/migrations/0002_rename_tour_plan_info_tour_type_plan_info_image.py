# Generated by Django 5.2.4 on 2025-08-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan_info',
            old_name='tour',
            new_name='tour_type',
        ),
        migrations.AddField(
            model_name='plan_info',
            name='image',
            field=models.ImageField(blank=True, upload_to='destinations/'),
        ),
    ]
