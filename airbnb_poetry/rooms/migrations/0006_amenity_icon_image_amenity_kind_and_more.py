# Generated by Django 4.1.2 on 2023-06-26 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0005_alter_room_amenities_alter_room_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="amenity",
            name="icon_image",
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="amenity",
            name="kind",
            field=models.CharField(
                choices=[
                    ("view", "전망"),
                    ("bath_room", "욕실"),
                    ("bed_room_and_laundry", "침실 및 세탁 시설"),
                    ("entertainment", "엔터테인먼트"),
                    ("air_conditioning", "냉난방"),
                    ("safety", "숙소 안전"),
                    ("work_space", "인터넷 및 작업 공간"),
                    ("kichen_and_dining", "주방 및 식당"),
                    ("location", "위치 특성"),
                    ("park_and_etc", "주차장 및 기타 시설"),
                    ("service", "서비스"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="amenity",
            name="description",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
