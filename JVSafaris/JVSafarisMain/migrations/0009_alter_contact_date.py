# Generated by Django 4.1.3 on 2022-12-11 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JVSafarisMain', '0008_package_kids_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 11, 1, 8, 9, 692973)),
        ),
    ]