# Generated by Django 5.1.4 on 2024-12-31 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lesson", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lesson",
            old_name="youtube_Url",
            new_name="youtube_url",
        ),
    ]
