# Generated by Django 4.2.1 on 2023-06-24 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItem',
            new_name='LoginModel',
        ),
    ]