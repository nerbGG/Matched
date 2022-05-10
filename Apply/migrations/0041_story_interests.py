# Generated by Django 3.2.12 on 2022-05-10 04:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0040_auto_20220510_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('tech', 'Technology'), ('eng', 'Engineering'), ('bio', 'Biology'), ('art', 'Art'), ('ath', 'Athletics'), ('fin', 'Finance'), ('bus', 'Business')], max_length=28),
        ),
    ]
