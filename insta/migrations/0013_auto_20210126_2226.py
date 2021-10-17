# Generated by Django 3.1.5 on 2021-01-26 22:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0012_auto_20210126_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_linked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='insta.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.profile'),
        ),
    ]