# Generated by Django 5.1.2 on 2024-10-21 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_rename_created_at_meal_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='data',
            new_name='date',
        ),
    ]
