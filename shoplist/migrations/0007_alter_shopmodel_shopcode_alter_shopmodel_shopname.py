# Generated by Django 4.2.2 on 2023-07-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplist', '0006_alter_shopmodel_shopcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopmodel',
            name='shopCode',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='shopmodel',
            name='shopname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]