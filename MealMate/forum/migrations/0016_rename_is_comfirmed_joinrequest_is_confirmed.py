# Generated by Django 5.1.2 on 2024-10-19 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0015_joinrequest_sponser"),
    ]

    operations = [
        migrations.RenameField(
            model_name="joinrequest",
            old_name="is_comfirmed",
            new_name="is_confirmed",
        ),
    ]