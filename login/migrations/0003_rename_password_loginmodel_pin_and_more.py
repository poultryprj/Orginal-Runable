# Generated by Django 4.2.1 on 2023-06-24 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_cartitem_loginmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginmodel',
            old_name='password',
            new_name='PIN',
        ),
        migrations.RenameField(
            model_name='loginmodel',
            old_name='username',
            new_name='USER_MOBILE_NO',
        ),
    ]