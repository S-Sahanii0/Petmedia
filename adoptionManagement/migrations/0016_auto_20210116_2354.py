# Generated by Django 3.1 on 2021-01-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionManagement', '0015_auto_20210115_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='gender',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='dog_age',
            field=models.CharField(max_length=60),
        ),
    ]
