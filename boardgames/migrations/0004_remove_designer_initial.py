# Generated by Django 2.1.3 on 2018-12-02 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0003_auto_20181202_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designer',
            name='initial',
        ),
    ]
