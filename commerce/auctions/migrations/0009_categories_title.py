# Generated by Django 4.0.1 on 2022-01-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='title',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
