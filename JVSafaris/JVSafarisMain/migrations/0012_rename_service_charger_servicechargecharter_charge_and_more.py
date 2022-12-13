# Generated by Django 4.1.3 on 2022-12-13 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JVSafarisMain', '0011_packagecharter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicechargecharter',
            old_name='service_charger',
            new_name='charge',
        ),
        migrations.RemoveField(
            model_name='servicechargecharter',
            name='category',
        ),
        migrations.RemoveField(
            model_name='servicechargecharter',
            name='service_item',
        ),
        migrations.RemoveField(
            model_name='serviceitem',
            name='price',
        ),
        migrations.AlterField(
            model_name='servicechargecharter',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JVSafarisMain.serviceitem'),
        ),
    ]