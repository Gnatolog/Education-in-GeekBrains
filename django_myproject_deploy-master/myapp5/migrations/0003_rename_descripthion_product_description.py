# Generated by Django 5.0.4 on 2024-04-28 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0002_product_date_added_product_descripthion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descripthion',
            new_name='description',
        ),
    ]