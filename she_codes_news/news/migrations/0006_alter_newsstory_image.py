# Generated by Django 4.2.2 on 2023-07-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_newsstory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.URLField(default='https://picsum.photos/600'),
        ),
    ]
