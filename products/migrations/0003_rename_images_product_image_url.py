# Generated by Django 3.2 on 2024-03-03 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_rename_image_url_product_images"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="images",
            new_name="image_url",
        ),
    ]
