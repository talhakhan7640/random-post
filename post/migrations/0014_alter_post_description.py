# Generated by Django 3.2.7 on 2021-10-31 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_post_content_video_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]