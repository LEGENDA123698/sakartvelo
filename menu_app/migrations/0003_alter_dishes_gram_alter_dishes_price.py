# Generated by Django 5.1.4 on 2025-01-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_alter_dishes_gram_alter_dishes_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='gram',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='price',
            field=models.CharField(max_length=4),
        ),
    ]
