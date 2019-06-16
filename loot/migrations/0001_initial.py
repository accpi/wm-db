# Generated by Django 2.2.2 on 2019-06-16 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mission', '0006_auto_20190616_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rarity', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Loot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mission.Mission')),
                ('rarity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot.Rarity')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loot.Type')),
            ],
        ),
    ]
