# Generated by Django 5.1.2 on 2024-10-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0010_grouppost_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grouppost",
            name="address",
            field=models.CharField(max_length=40),
        ),
    ]