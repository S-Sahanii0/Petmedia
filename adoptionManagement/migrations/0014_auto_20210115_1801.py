# Generated by Django 3.1 on 2021-01-15 12:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionManagement', '0013_auto_20210115_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='id',
        ),
        migrations.AlterField(
            model_name='requests',
            name='dog',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='adoptionManagement.dog'),
            preserve_default=False,
        ),
    ]
