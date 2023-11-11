# Generated by Django 4.2.7 on 2023-11-11 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watermark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatermarkedVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.IntegerField(default=0)),
                ('position_y', models.IntegerField(default=0)),
                ('extraction_timestamp', models.DateTimeField(auto_now_add=True)),
                ('watermark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watermark.watermark')),
            ],
        ),
    ]
