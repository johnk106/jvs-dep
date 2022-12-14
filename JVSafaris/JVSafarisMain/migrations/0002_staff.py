# Generated by Django 4.1.3 on 2022-12-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JVSafarisMain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('twitter', models.CharField(blank=True, max_length=1000)),
                ('facebook', models.CharField(blank=True, max_length=1000)),
                ('instagram', models.CharField(blank=True, max_length=1000)),
                ('linkedin', models.CharField(blank=True, max_length=1000)),
                ('isEstemeed', models.BooleanField()),
            ],
        ),
    ]
