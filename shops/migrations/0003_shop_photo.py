# Generated by Django 4.0.5 on 2022-06-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_category_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
