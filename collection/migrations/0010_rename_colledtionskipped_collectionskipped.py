# Generated by Django 4.2.2 on 2023-08-29 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_roleid_userroles_roleid'),
        ('collection', '0009_colledtionskipped'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='colledtionSkipped',
            new_name='collectionSkipped',
        ),
    ]
