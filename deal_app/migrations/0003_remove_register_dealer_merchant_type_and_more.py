# Generated by Django 4.2.5 on 2024-07-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal_app', '0002_alter_model_add_fields_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_dealer',
            name='merchant_type',
        ),
        migrations.AddField(
            model_name='register_dealer',
            name='drop_merchant_type',
            field=models.CharField(choices=[('hotel', 'Hotel'), ('restuarent', 'Restuarent'), ('spa', 'Spa'), ('saloon', 'Saloon')], max_length=30, null=True),
        ),
    ]