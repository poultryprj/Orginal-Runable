# Generated by Django 4.2.2 on 2023-08-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplist', '0008_rename_shopname_shopmodel_shoparea_shopmodel_shopid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopmodel',
            name='shopAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shopAlternateNo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shopDistance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shopFlexibleRate',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shopMobileNo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shopOwnerId',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shopPincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shopStatus',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shopType',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
