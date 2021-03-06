# Generated by Django 3.0.9 on 2021-05-02 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prime', '0008_auto_20210502_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='sharer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
