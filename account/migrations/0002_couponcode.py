# Generated by Django 3.0.9 on 2021-04-12 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('valid', models.BooleanField()),
                ('active', models.BooleanField()),
            ],
        ),
    ]
