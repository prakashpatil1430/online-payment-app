# Generated by Django 5.0 on 2024-01-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='country',
            field=models.CharField(choices=[('united status', 'United States'), ('united kingdom', 'United Kingdom'), ('canada', 'Canada'), ('australia', 'Australia'), ('india', 'India')], default='', max_length=50),
        ),
    ]
