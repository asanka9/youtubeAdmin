# Generated by Django 3.0.5 on 2020-08-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_auto_20200816_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolessons',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
