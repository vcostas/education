# Generated by Django 2.1 on 2019-01-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemessage', '0002_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch',
            name='dispatch_status',
            field=models.PositiveIntegerField(choices=[(1, 'Pending'), (5, 'Processing'), (2, 'Sent'), (3, 'Error'), (4, 'Failed')], default=1, verbose_name='Dispatch status'),
        ),
    ]