# Generated by Django 5.0 on 2023-12-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default='default_value_here', max_length=255),
        ),
    ]