# Generated by Django 4.0.5 on 2022-07-05 03:45

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('shops', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
