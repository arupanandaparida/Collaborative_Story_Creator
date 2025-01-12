# Generated by Django 4.2 on 2024-08-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_remove_story_contributions_count_story_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='category',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_url',
        ),
        migrations.AddField(
            model_name='story',
            name='contributions_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
