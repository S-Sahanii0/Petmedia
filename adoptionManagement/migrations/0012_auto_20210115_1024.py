# Generated by Django 3.1 on 2021-01-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionManagement', '0011_auto_20210114_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionqueue',
            name='dog_name',
            field=models.CharField(max_length=60, null=True, verbose_name='Breed'),
        ),
        migrations.AlterField(
            model_name='adoptionqueue',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/', verbose_name='Picture of the dog'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='status',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='requests',
            name='is_requested',
            field=models.BooleanField(default=False),
        ),
    ]
