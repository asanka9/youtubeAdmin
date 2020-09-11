# Generated by Django 3.0.5 on 2020-08-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_completed_ischecked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videolessons',
            options={'ordering': ['countValue']},
        ),
        migrations.AddField(
            model_name='videolessons',
            name='countValue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='videolessons',
            name='isImage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videolessons',
            name='isWeb',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='videolessons',
            name='chanel',
            field=models.CharField(default='unknown', max_length=128),
        ),
    ]
