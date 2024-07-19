# Generated by Django 3.2.25 on 2024-07-19 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, unique=True)),
                ('country', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField(max_length=500)),
                ('contact_info', models.CharField(max_length=200)),
                ('opening_hours', models.TextField(max_length=200)),
                ('special_features', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Café', 'Café'), ('Club', 'Club'), ('Support Center', 'Support Center')], max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.city')),
            ],
        ),
    ]
