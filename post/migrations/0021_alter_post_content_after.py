# Generated by Django 3.2.7 on 2021-11-01 10:10

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_post_content_after'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_after',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True),
        ),
    ]