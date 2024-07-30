# Generated by Django 4.2.5 on 2024-07-17 08:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='model_add_fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.TimeField(default=datetime.time(9, 0))),
                ('end_time', models.TimeField()),
                ('item_img', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='register_dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_name', models.CharField(max_length=255)),
                ('merchant_type', models.CharField(max_length=30, null=True)),
                ('merchant_address', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=40, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
