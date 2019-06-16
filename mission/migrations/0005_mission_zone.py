# Generated by Django 2.2.2 on 2019-06-16 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0004_remove_mission_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='zone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mission.Zone'),
            preserve_default=False,
        ),
    ]
