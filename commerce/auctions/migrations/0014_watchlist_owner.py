# Generated by Django 4.0.1 on 2022-02-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_listing_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='owner',
            field=models.IntegerField(default=-1),
        ),
    ]
