# Generated by Django 2.1.2 on 2018-12-16 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_remove_post_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to='auction_pics'),
        ),
    ]