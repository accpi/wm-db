# Generated by Django 2.2.2 on 2019-06-16 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0003_auto_20190616_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='zone',
        ),
    ]
