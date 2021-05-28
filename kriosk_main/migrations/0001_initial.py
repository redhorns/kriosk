# Generated by Django 3.1 on 2021-02-02 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('client_tagline', models.TextField(blank=True, null=True)),
                ('services', models.TextField(blank=True, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='portfolio')),
                ('image_side', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]