# Generated by Django 4.2.4 on 2023-08-25 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_music', '0003_user_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_favorite',
        ),
    ]