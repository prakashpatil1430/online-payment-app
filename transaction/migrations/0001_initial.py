# Generated by Django 5.0 on 2024-01-05 03:53

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=15, max_length=20, prefix='TRN', unique=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('failed', 'failed'), ('completed', 'completed'), ('pending', 'pending'), ('processing', 'processing'), ('request_sent', 'request_sent'), ('request_settled', 'request settled'), ('request_processing', 'request processing')], default='pending', max_length=100)),
                ('transaction_type', models.CharField(choices=[('transfer', 'Transfer'), ('recieved', 'Recieved'), ('withdraw', 'withdraw'), ('refund', 'Refund'), ('request', 'Payment Request'), ('none', 'None')], default='none', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
