# Generated by Django 4.0.1 on 2022-02-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_listing_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='owner',
            field=models.IntegerField(default=-1),
        ),
    ]