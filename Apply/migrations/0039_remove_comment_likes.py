# Generated by Django 3.2.12 on 2022-05-10 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0038_auto_20220510_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]
