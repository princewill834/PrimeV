# Generated by Django 3.0.9 on 2021-04-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0005_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]