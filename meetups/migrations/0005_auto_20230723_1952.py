# Generated by Django 3.2.20 on 2023-07-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_auto_20230723_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-04-22'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='rohit@gmail.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
