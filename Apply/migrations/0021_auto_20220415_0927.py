# Generated by Django 3.2.12 on 2022-04-15 13:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0020_alter_profile_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='resume',
        ),
        migrations.AddField(
            model_name='jobs',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('tech', 'Technology'), ('med', 'Medical'), ('art', 'Art'), ('ath', 'Athletics'), ('fin', 'Finance'), ('bus', 'Business')], max_length=24),
        ),
    ]