# Generated by Django 3.1 on 2021-01-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_section',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
