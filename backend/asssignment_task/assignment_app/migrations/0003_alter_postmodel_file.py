# Generated by Django 4.1.7 on 2023-03-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_app', '0002_postmodel_file_postmodel_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='file',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='uploads/'),
        ),
    ]
