# Generated by Django 3.1 on 2021-01-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionManagement', '0016_auto_20210116_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionqueue',
            name='gender',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
