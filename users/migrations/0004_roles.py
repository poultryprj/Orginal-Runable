# Generated by Django 4.2.2 on 2023-08-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userroles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('roleId', models.IntegerField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
