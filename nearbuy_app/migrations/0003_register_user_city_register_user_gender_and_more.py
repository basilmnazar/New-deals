# Generated by Django 4.2.5 on 2024-07-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nearbuy_app', '0002_remove_register_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_user',
            name='city',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='register_user',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='register_user',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
    ]