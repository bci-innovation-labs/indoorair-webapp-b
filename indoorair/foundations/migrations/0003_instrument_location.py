# Generated by Django 2.2.7 on 2019-11-19 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundations', '0002_instrument_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='location',
            field=models.CharField(default='test', max_length=127),
            preserve_default=False,
        ),
    ]
