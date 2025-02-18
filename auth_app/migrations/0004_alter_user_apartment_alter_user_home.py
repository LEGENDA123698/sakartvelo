# Generated by Django 5.1.4 on 2025-02-17 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_alter_user_apartment_alter_user_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apartment',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='home',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)]),
        ),
    ]
