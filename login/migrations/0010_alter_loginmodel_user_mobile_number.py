# Generated by Django 4.2.2 on 2023-07-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_loginmodel_user_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='user_mobile_number',
            field=models.IntegerField(null=True),
        ),
    ]
