# Generated by Django 3.1 on 2021-02-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_auto_20210202_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='home')),
            ],
        ),
    ]
