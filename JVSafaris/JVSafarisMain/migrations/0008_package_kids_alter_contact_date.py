# Generated by Django 4.1.3 on 2022-12-11 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JVSafarisMain', '0007_packagecategory_alter_contact_date_package_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='kids',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 11, 1, 7, 57, 457142)),
        ),
    ]
