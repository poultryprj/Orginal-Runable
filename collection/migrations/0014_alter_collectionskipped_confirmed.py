# Generated by Django 4.2.2 on 2023-08-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0013_alter_collectionskipped_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionskipped',
            name='confirmed',
            field=models.TextField(),
        ),
    ]
