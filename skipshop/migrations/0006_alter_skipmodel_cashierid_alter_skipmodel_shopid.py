# Generated by Django 4.2.2 on 2023-07-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipshop', '0005_alter_skipmodel_cashierid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skipmodel',
            name='cashierId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='skipmodel',
            name='shopId',
            field=models.IntegerField(null=True),
        ),
    ]