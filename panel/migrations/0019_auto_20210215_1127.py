# Generated by Django 3.1 on 2021-02-15 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0018_delete_our_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='our_team',
            name='sm1',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='sm1_icon',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='sm1_url',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='sm2',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='sm2_icon',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='sm2_url',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='sm3',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='sm3_icon',
        ),
        migrations.RemoveField(
            model_name='our_team',
            name='sm3_url',
        ),
    ]