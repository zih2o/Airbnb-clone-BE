# Generated by Django 4.1.2 on 2023-06-26 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_amenity_icon_image_amenity_kind_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="amenity",
            name="description",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
