# Generated by Django 3.2.9 on 2021-11-11 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fe_app', '0002_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Thread',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='topic',
            new_name='thread',
        ),
    ]