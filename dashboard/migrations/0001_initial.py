# Generated by Django 4.2.2 on 2023-07-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dashboardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CashierId', models.CharField(max_length=1000)),
                ('RouteId', models.CharField(max_length=1000)),
            ],
        ),
    ]
