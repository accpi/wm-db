# Generated by Django 2.2.2 on 2019-06-16 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loot',
            name='attunement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='loot',
            name='text',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]