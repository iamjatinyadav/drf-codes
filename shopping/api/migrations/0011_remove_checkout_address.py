# Generated by Django 4.1.3 on 2022-12-13 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='address',
        ),
    ]