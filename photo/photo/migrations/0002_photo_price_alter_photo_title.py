# Generated by Django 4.1.5 on 2023-01-11 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='price',
            field=models.IntegerField(default=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
