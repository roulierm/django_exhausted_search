# Generated by Django 3.2.9 on 2021-11-28 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_userpost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='title',
        ),
    ]