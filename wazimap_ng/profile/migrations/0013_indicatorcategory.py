# Generated by Django 2.2.10 on 2020-04-11 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0077_auto_20200411_2044'),
        ('profile', '0012_profileindicator'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='IndicatorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Profile')),
            ],
            options={
                'verbose_name_plural': 'Indicator Categories',
                'ordering': ['id'],
            },
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
