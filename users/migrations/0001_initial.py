# Generated by Django 4.2.2 on 2023-08-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('userName', models.CharField(max_length=20, null=True)),
                ('userMobileNo', models.PositiveBigIntegerField(null=True)),
                ('userAlternateNo', models.IntegerField(null=True)),
                ('userPassword', models.IntegerField(null=True)),
                ('userLevel', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
