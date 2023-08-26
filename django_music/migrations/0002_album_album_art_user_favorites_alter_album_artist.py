# Generated by Django 4.2.4 on 2023-08-25 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_art',
            field=models.ImageField(default='media/unavailable.jpg', upload_to='media/'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(to='django_music.album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='django_music.artist'),
        ),
    ]