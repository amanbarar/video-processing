# Generated by Django 4.2.7 on 2023-11-16 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermark', '0003_alter_watermark_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='watermarkedvideos',
            name='processed_video',
            field=models.FileField(default=None, null=True, upload_to='watermark/processed_video/'),
        ),
    ]
