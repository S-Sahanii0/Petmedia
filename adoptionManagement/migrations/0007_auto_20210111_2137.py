# Generated by Django 3.1 on 2021-01-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionManagement', '0006_auto_20210111_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
