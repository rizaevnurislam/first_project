# Generated by Django 4.2.15 on 2025-01-05 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_products_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
