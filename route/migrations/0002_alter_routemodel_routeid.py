# Generated by Django 4.2.2 on 2023-07-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routemodel',
            name='RouteId',
            field=models.IntegerField(null=True),
        ),
    ]
