# Generated by Django 4.2.4 on 2023-08-28 16:32

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='blog')),
                ('created_date', models.DateTimeField(default=datetime.datetime(2023, 8, 28, 16, 32, 21, 461285, tzinfo=datetime.timezone.utc))),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]