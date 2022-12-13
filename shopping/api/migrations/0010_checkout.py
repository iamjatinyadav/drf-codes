# Generated by Django 4.1.3 on 2022-12-13 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_alter_cartitems_count_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('payment', models.IntegerField(choices=[(1, 'Paypal'), (2, 'Direct Check'), (3, 'Bank Transfer')], default=1)),
                ('product', models.JSONField()),
                ('total', models.IntegerField(default=0)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to='api.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Checkout',
                'verbose_name_plural': 'Checkouts',
                'db_table': 'Checkout',
                'managed': True,
            },
        ),
    ]