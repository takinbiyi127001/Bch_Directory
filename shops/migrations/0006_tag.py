# Generated by Django 4.0.5 on 2022-06-27 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_shop_countries_shop_is_closed_temporarily_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='shops.shop')),
            ],
        ),
    ]
