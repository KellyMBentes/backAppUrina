# Generated by Django 2.2.11 on 2020-04-17 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='option',
            old_name='notificationId',
            new_name='notification',
        ),
    ]
