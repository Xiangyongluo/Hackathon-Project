# Generated by Django 3.0.8 on 2020-07-27 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='filesUp',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]