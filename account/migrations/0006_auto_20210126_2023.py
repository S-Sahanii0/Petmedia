# Generated by Django 3.1 on 2021-01-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210124_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='dog.jpg', upload_to='profile/'),
        ),
    ]