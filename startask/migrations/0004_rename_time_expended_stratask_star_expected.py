# Generated by Django 4.0 on 2021-12-26 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startask', '0003_stratask_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stratask',
            old_name='time_expended',
            new_name='star_expected',
        ),
    ]
