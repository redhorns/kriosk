# Generated by Django 3.1 on 2021-02-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0014_auto_20210211_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]