# Generated by Django 3.2.8 on 2021-11-08 18:09

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='img',
            field=models.ImageField(default='user_img.png', storage=django.core.files.storage.FileSystemStorage(base_url='/images', location='/account/media/images'), upload_to='images/'),
        ),
    ]
