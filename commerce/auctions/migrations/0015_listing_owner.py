# Generated by Django 4.0.1 on 2022-02-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_watchlist_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.IntegerField(default=-1),
        ),
    ]