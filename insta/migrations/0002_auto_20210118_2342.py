# Generated by Django 3.1.5 on 2021-01-18 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='loation',
            new_name='location',
        ),
    ]