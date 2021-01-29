# Generated by Django 3.1 on 2021-01-25 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_section_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('read_duration', models.IntegerField(blank=True, null=True)),
                ('tag', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.blog_section')),
            ],
        ),
    ]