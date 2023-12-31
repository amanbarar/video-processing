# Generated by Django 4.2.7 on 2023-11-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_extraction', '0004_audioextraction_extraction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='audioextraction',
            name='audio',
            field=models.FileField(default=None, null=True, upload_to='audio_extraction/output/'),
        ),
        migrations.AlterField(
            model_name='audioextraction',
            name='video',
            field=models.FileField(default=None, null=True, upload_to='audio_extraction/input/'),
        ),
    ]
