# Generated by Django 3.1 on 2021-02-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0004_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='position_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
