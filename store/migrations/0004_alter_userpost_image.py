# Generated by Django 3.2.9 on 2021-11-28 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_userpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]