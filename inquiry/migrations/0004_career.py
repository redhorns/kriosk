# Generated by Django 3.1 on 2021-02-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0003_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(blank=True, max_length=200, null=True)),
                ('position_number', models.IntegerField(blank=True, max_length=200, null=True)),
                ('position_requirement', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
