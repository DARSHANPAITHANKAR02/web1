# Generated by Django 3.1 on 2020-08-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
    ]