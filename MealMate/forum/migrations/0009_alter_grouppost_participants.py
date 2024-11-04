# Generated by Django 5.1.2 on 2024-10-19 04:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0008_postimage_remove_post_imaged_post_images"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="grouppost",
            name="participants",
            field=models.ManyToManyField(
                related_name="joined_user", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]