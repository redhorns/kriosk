# Generated by Django 3.1 on 2021-02-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0009_auto_20210210_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes'),
        ),
    ]
