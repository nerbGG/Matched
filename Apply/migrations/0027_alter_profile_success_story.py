# Generated by Django 3.2.12 on 2022-04-22 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0026_auto_20220415_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='success_story',
            field=models.TextField(blank=True, max_length=8000),
        ),
    ]
