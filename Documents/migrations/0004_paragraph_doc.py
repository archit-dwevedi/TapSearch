# Generated by Django 2.2.7 on 2019-11-23 11:36

import Documents.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0003_paragraph_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='doc',
            field=models.FileField(blank=True, null=True, upload_to=Documents.models.upload_image_path),
        ),
    ]