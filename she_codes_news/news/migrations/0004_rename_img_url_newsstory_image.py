# Generated by Django 4.2.2 on 2023-07-18 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_newsstory_img_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newsstory", old_name="img_url", new_name="image",
        ),
    ]
