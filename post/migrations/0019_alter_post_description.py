# Generated by Django 3.2.7 on 2021-11-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_alter_post_content_video_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
