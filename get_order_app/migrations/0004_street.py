# Generated by Django 5.1.4 on 2025-02-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_order_app', '0003_resultsolution_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
