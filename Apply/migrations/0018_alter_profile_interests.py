# Generated by Django 3.2.12 on 2022-04-12 14:51

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0017_auto_20220411_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('tech', 'Technology'), ('med', 'Medical'), ('art', 'Art'), ('ath', 'Athletics'), ('fin', 'Finance'), ('bus', 'Business')], max_length=24),
        ),
    ]