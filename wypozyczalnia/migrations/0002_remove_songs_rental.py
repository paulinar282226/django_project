# Generated by Django 4.0.5 on 2022-06-10 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='rental',
        ),
    ]
