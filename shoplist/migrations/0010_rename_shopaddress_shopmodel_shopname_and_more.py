# Generated by Django 4.2.2 on 2023-08-24 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplist', '0009_shopmodel_shopaddress_shopmodel_shopalternateno_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopmodel',
            old_name='shopAddress',
            new_name='shopname',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopAlternateNo',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopArea',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopDistance',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopFlexibleRate',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopId',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopLatitude',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopLongitude',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopMobileNo',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopName',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopOwnerId',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopPincode',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopStatus',
        ),
        migrations.RemoveField(
            model_name='shopmodel',
            name='shopType',
        ),
        migrations.AlterField(
            model_name='shopmodel',
            name='shopCode',
            field=models.CharField(max_length=500, null=True),
        ),
    ]