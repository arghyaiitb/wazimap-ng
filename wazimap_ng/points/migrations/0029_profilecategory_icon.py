# Generated by Django 2.2.10 on 2020-06-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0028_coordinatefile_collection_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilecategory',
            name='icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]