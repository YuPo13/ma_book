# Generated by Django 3.0.2 on 2020-01-15 22:02

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200115_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.content_file_name),
        ),
    ]
