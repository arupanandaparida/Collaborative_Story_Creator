# Generated by Django 4.2 on 2024-08-19 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='contributions_count',
            field=models.IntegerField(default=0),
        ),
    ]
