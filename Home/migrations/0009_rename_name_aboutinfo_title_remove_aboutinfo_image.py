# Generated by Django 4.0.3 on 2022-09-19 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_comingsoon_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutinfo',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='aboutinfo',
            name='image',
        ),
    ]
