# Generated by Django 4.0.3 on 2022-09-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantinfo',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]