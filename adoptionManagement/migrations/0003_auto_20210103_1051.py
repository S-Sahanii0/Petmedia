# Generated by Django 3.1 on 2021-01-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionManagement', '0002_dog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionqueue',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted')], max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted')], max_length=60, null=True),
        ),
    ]
