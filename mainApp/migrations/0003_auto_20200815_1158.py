# Generated by Django 3.0.5 on 2020-08-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_videolessons_isvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]