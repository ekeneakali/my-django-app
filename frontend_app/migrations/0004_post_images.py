# Generated by Django 3.1.1 on 2022-02-07 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_app', '0003_remove_post_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/', verbose_name='upload a photo'),
            preserve_default=False,
        ),
    ]
