# Generated by Django 4.2.8 on 2023-12-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_item_category_item_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="slug",
            field=models.SlugField(default="test-product"),
            preserve_default=False,
        ),
    ]
