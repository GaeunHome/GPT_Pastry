# Generated by Django 4.1.4 on 2023-05-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastry',
            name='image',
            field=models.ImageField(default=False, upload_to='images/'),
        ),
    ]
