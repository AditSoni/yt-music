# Generated by Django 3.0 on 2019-12-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_title', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=264, unique=True)),
                ('song_url', models.URLField(unique=True)),
                ('song_path', models.FilePathField(unique=True)),
            ],
        ),
    ]
