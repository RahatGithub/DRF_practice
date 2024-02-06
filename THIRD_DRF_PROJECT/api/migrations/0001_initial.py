# Generated by Django 5.0.1 on 2024-02-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('dept', models.CharField(max_length=50)),
                ('cgpa', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
    ]