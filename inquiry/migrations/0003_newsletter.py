# Generated by Django 3.1 on 2021-02-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_remove_contact_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
