# Generated by Django 5.1.3 on 2025-03-03 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='added_at',
        ),
    ]
