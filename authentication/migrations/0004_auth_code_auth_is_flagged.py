# Generated by Django 3.1 on 2021-02-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210201_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth_code',
            name='auth_is_flagged',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
