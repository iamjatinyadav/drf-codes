# Generated by Django 4.1.3 on 2022-11-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
                'db_table': 'Notes',
                'managed': True,
            },
        ),
    ]
