# Generated by Django 4.2.5 on 2023-09-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_district_province_ward_delete_studentmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='did',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='pid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ward',
            name='wid',
            field=models.IntegerField(null=True),
        ),
    ]
