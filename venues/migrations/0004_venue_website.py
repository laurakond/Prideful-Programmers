# Generated by Django 4.2.14 on 2024-07-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0003_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='website',
            field=models.URLField(default='https://thegeorge.ie'),
            preserve_default=False,
        ),
    ]
